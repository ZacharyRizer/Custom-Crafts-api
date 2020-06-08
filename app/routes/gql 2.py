from flask import Blueprint, Flask, request
import json
from ..schema import schema

bp = Blueprint('gql', __name__, url_prefix='')


@bp.route('/graphql', methods=['GET', 'POST'])
def graphql():
    print(f'req : {request}')
    data = json.loads(request.data)
    print(f'data:  {data}')
    print(f'exec:  {schema.execute()}')
    # return 'hi'
    val = schema.execute(data['query'])
    print(f'val: ', val)
    return 'val'
    # return json.dumps(schema.execute(data['query'].data))
