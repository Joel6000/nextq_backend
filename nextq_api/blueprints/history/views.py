from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from models.history import History
from models.user import User
from models.store import Store
import datetime

history_api_blueprint = Blueprint('history_api',
                             __name__,
                             template_folder='templates')



@history_api_blueprint.route('/<user_id>/user/<store_id>/store', methods=['POST'])
def create(user_id, store_id):
    new_history = History(
        user = User.get_or_none(User.id == user_id),
        store = Store.get_or_none(Store.id == store_id)
    )

    if new_history.save():
        return jsonify({
            "user":new_history.user.name,
            "store":new_history.store.name
            })
    else:
        return jsonify([err for err in new_history.errors])


@history_api_blueprint.route('/<user_id>/user/<store_id>/store/update', methods=['POST'])
def update(user_id, store_id):
    history = History.get_or_none((History.user_id == user_id) & (History.store_id == store_id) )
    history.time_out = datetime.datetime.now()
    print("before save")
    if history.save():
        print("after save")
        return jsonify({
            "time_out":history.time_out,
            "user":history.user.name,
            "store":history.store.name
            })
    else:
        return jsonify([err for err in new_history.errors])
