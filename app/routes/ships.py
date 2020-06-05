from flask import Blueprint

bp = Blueprint('ships', __name__, url_prefix='/ships')


@bp.route('/')
def login():
    return {'test': 'ships'}