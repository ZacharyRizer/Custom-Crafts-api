from flask import Blueprint, Flask, request
import json
from ..schema import schema

bp = Blueprint('ships', __name__, url_prefix='/ships')
# print(f'schema: {schema}')
# print(f'execute: ' {schema.execute()})

@bp.route('/', methods=['GET', 'POST'])
def testRoot():
    print(f'schema: {schema}')
    print(f'execute:  {schema.execute()}')
    return {'test': 'ships1'}
