from flask import Flask
from flask_graphql import GraphQLView
from .schema import schema

from .config import Configuration
from .models import db
from .routes import customers, ships, gql
from flask_migrate import Migrate

app = Flask(__name__)
# app.config.from_object(Configuration)
# app.register_blueprint(customers.bp)
# app.register_blueprint(ships.bp)
# app.register_blueprint(gql.bp)
# db.init_app(app)
# Migrate(app, db)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql',
                                                           schema=schema,
                                                           graphiql=True))
