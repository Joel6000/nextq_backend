from flask import Blueprint, jsonify, request, Response
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from models.user import User
import datetime

#AUTHORISATION API, SIMILAR TO NEXTAGRAM SIGN UP. USE CHECK_PASSWORD_HASH FOR PASSWORLD VALIDATION.
auth_api_blueprint = Blueprint('auth_api',
                             __name__,
                             template_folder='templates')

@auth_api_blueprint.route('/user', methods=['POST'])
def login():
    params = request.json
    user = User.get_or_none(User.mobile == params.get('mobile'))
    if user:
        authorised = check_password_hash(user.password_hash,params.get('password'))
        if  authorised:
            access_token = create_access_token(identity = str(user.id))
            return {
                'token': access_token,
                'name':user.name,
                'mobile':user.mobile,
                'user_id':user.id
                }
        else:
            return {'error': 'Email or password invalid'}
    
        