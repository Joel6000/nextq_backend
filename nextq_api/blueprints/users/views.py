from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from models import User

users_api_blueprint = Blueprint('users_api',
                             __name__,
                             template_folder='templates')

@users_api_blueprint.route('/new', methods=['POST'])
def create():
    params = request.json
    new_user = User(
        name = params.get("username"), 
        email=params.get("email"), 
        password=params.get("password"),
        mobile=params.get("mobilehp")
        )

    if new_user.save():
        token = create_access_token(identity = new_user.id)
        return jsonify({"token":token})
    else:
        return jsonify([err for err in new_user.errors])

@users_api_blueprint.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get_or_none(user.id == user_id)

    if user:
        token = create_access_token(identity = user.id)
        return jsonify({"token":token})
    else:
        return jsonify([err for err in new_user.errors])

@users_api_blueprint.route('/<user_id>/checkin', methods=['POST'])
def user_checkin(user_id):
    user = User.get_or_none(user.id == user_id)

    if user:
        pass
    else:
        pass