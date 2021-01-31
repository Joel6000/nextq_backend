from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from models.history import History
from models.user import User
from models.store import Store

history_api_blueprint = Blueprint('history_api',
                             __name__,
                             template_folder='templates')



@history_api_blueprint.route('/new', methods=['POST'])
def create():
    params = request.json
    new_history = History(
        user = params.get("name"),
        store = params.get("location"), 
        )

    if new_history.save():
        token = create_access_token(identity = new_history.id) #somehting else here
        return jsonify({"token":token})
    else:
        return jsonify([err for err in new_history.errors])