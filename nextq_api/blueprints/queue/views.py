from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models.history import History
from models.user import User
from models.store import Store
from models.queue import Queue
import datetime

queue_api_blueprint = Blueprint('queue_api',
                             __name__,
                             template_folder='templates')


@queue_api_blueprint.route('/<user_id>/user/<store_id>/store', methods=['POST'])
def create(user_id, store_id):
    store = Store.get_by_id(store_id)
    user = User.get_by_id(user_id)

    space_available = int(store.limit - shop.headcount)

    if space_available < 0:
        new_queue = Queue(
            user=user,
            store=store
        )

        if new_queue.save():
            return jsonify({
                "user":new_queue.store,
                "store":new_queue.store
            })
        else:
            return jsonify([err for err in new_history.errors])
    else:
        return jsonify({"errors":"Space is available, queue function skipped."})



# query = queue.select().where(shop.id = blabla) → [1, a, cbde, were, 2325, 6, 7, 8, 9, 10]
# notify(space_available, query)

# def notify(space_available, query):
#     for i in range(0:space_available):
#         alert(query[i+5])
