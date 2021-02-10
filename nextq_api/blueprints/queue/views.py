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


def get_queue(user_id):
    queue = Queue.get_or_none(Queue.user_id == user_id)

    if queue:
        queue_list = Queue.select().where(Queue.store_id == queue.store_id)

        if queue_list:
            queue_number = 0
            for index, user_queue in enumerate(queue_list):
                if user_queue.user_id == queue.user_id:
                    queue_number = index + 1
            return queue_number

        else:
            return 0

    else:
        return 0 

def get_space(user_id):
    from models.store import Store
    queue = Queue.get_or_none(Queue.user_id == user_id)
    
    if queue:
        store = Store.get_by_id(queue.store_id)
        space = store.customer_limit - store.headcount
        return space
    else:
        return -1


# Manually delete person from queue
@queue_api_blueprint.route('/<user_id>/user/<store_id>/store/delete', methods=['POST'])
def delete(user_id, store_id):

    store = Store.get_by_id(store_id)
    user = User.get_by_id(user_id)

    queue = Queue.get_or_none((Queue.user_id == user.id) & (Queue.store_id == store.id))

    if queue.delete_instance():
        store.queue -= 1
        store.save()
        return jsonify({"msg":"Successfully deleted queue"})
    else:
        return jsonify([err for err in queue.errors])


#GET QUEUE NUMBER
@queue_api_blueprint.route("/<user_id>/", methods = ["GET"])
def get_number(user_id):
    queue_number = get_queue(user_id)
    space_available = get_space(user_id)
    
    if queue_number == 0:
        return jsonify({"error": "You are not in queue."})
    elif queue_number <= space_available: 
        return jsonify({
            "queue_number": queue_number, 
            "notification": "You can enter the store."
            })
    else:   #return notification
        return jsonify({
            "queue_number": queue_number, 
            "notification": "Please wait to enter the store."
            })


    
    
    
    

