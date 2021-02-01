from flask import Blueprint, jsonify, request, Response
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import check_password_hash
from models.user import User
import datetime


auth_api_blueprint = Blueprint('auth_api',
                             __name__,
                             template_folder='templates')

@auth_api_blueprint.route('/user', methods=['GET'])
def login():
    params = request.json
    user = User.get_or_none(User.mobile == params.get('mobile'))
    authorised = user.check_password_hash(params.get('password'))
    if not authorised:
        return {'error': 'Email or password invalid'}
    
    expires = datetime.timedelta(days=1)
    access_token = create_access_token(identity=user.id), expires_delta = expires)
    return {'token': access_token}