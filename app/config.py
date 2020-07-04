import os


class Configuration:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    S3_BUCKET = os.environ.get('S3_BUCKET')
    S3_SECRET = os.environ.get('S3_SECRET')
    S3_KEY_ID = os.environ.get('S3_KEY_ID')
    S3_REGION = os.environ.get('S3_REGION')
