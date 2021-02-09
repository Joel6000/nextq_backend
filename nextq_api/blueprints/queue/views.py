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

#GET QUEUE NUMBER
@queue_api_blueprint.route("/<user_id>/", methods = ["GET"])
def get_number(user_id):
    queue = Queue.get_or_none(Queue.user_id == user_id)

    if queue:
        queue_list = Queue.select().where(Queue.store_id == queue.store_id)

        if queue_list:
            queue_number = 0
            for index, user_queue in enumerate(queue_list):
                if user_queue.user_id == queue.user_id:
                    queue_number = index + 1
            return jsonify({"queue_number":queue_number}) 
            
        else:
            return jsonify({"message": "No Queue."})

    else:
        return jsonify({"queue_number":0}) 

