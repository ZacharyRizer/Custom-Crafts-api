from flask import Flask
from .config import Configuration
from .models import db
from .routes import customers, ships
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(customers.bp)
app.register_blueprint(ships.bp)
db.init_app(app)
Migrate(app, db)