from flask import Flask, jsonify
from flask_cors import cross_origin, CORS
from flask_migrate import Migrate
from .config import Configuration
from .models import db
from .auth import AuthError, requires_auth
from flask_graphql import GraphQLView
from .schema import schema


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    db.init_app(app)
    Migrate(app, db)

    @app.route('/', methods=["GET"])
    def wakeDyno():
        return 'Waking those Dinosaurs'

    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql',
                                                            schema=schema,
                                                            graphiql=True))



    # Error Handler
    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app




