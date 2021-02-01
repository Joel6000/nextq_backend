from flask import Blueprint, jsonify, request, Response
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import check_password_hash
from models.user import User


auth_api_blueprint = Blueprint('auth_api',
                             __name__,
                             template_folder='templates')

@auth_api_blueprint.route('/user', methods=['GET'])
def login():
    user = User.get_or_none(User.id == user_id)
    if user:
        token = create_access_token(identity = user.id)
        return jsonify({
            "username":user.name,
            "mobile":user.mobile,
            "email":user.email,
            "token":token
            })
    else:
        return jsonify([err for err in new_user.errors])