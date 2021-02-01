from flask import Blueprint, jsonify, request, Response
from flask_jwt_extended import create_access_token, jwt_required
from models.user import User

users_api_blueprint = Blueprint('users_api',
                             __name__,
                             template_folder='templates')

@users_api_blueprint.route('', methods=['POST'])
def create():
    params = request.json
    new_user = User(
        name = params.get("name"), 
        email=params.get("email"), 
        password=params.get("password"),
        mobile=params.get("mobile")
        )

    if new_user.save():
        token = create_access_token(identity = new_user.id)
        return jsonify({"token":token})
    else:
        return jsonify([err for err in new_user.errors])

@users_api_blueprint.route('/<user_id>', methods=['GET'])
def get_user(user_id):
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