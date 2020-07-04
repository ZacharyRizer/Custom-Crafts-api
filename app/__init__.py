from flask import Flask, jsonify, request
from flask_cors import cross_origin, CORS
from flask_migrate import Migrate
from .config import Configuration
from .models import db
from .auth import AuthError, requires_auth
from flask_graphql import GraphQLView
from .schema import schema
import boto3
import os
from werkzeug.utils import secure_filename


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    db.init_app(app)
    Migrate(app, db)

    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql',
                                                               schema=schema,
                                                               graphiql=True))

    @app.route('/upload-ship', methods=['POST'])
    def uploadShip():
        secret = os.environ.get('S3_SECRET')
        access_key = os.environ.get('S3_KEY_ID')
        region = os.environ.get('S3_REGION')
        bucket = os.environ.get('S3_BUCKET')

        s3 = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret
        )
        try:
            file = request.files['file']
            filename = ''
            if file:
                filename = secure_filename(file.filename)
                s3.upload_fileobj(
                    file,
                    bucket,
                    filename,
                    ExtraArgs={'ACL': 'public-read'}
                )
                return jsonify(f'https://{bucket}.s3.{region}.amazonaws.com/{filename}')
        except Exception as e:
            return (str(e))

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app
