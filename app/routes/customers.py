from flask import Blueprint

bp = Blueprint('users', __name__, url_prefix='/customers')


@bp.route('/')
def login():
    return {'test': 'users'}