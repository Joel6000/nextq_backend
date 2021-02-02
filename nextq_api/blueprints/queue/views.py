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


@queue_api_blueprint.route('/<user_id>/user/<store_id>/store/delete', methods=['POST'])
def delete(user_id, store_id):

    store = Store.get_by_id(store_id)
    user = User.get_by_id(user_id)

    queue = Queue.get_or_none((Queue.user_id == user.id) & (Queue.store_id == store.id))

    if queue.delete_instance():
        return jsonify({
                "msg":"Successfully deleted queue"})
    else:
        return jsonify([err for err in queue.errors])
  



# query = queue.select().where(shop.id = blabla) → [1, a, cbde, were, 2325, 6, 7, 8, 9, 10]
# notify(space_available, query)

# def notify(space_available, query):
#     for i in range(0:space_available):
#         alert(query[i+5])

#no physical queue, timer to boot out the queue if user doesn't checked in.