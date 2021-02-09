from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required #similar to login_required, a decorator to make sure that JWT token must be present for the function to be called
from models.history import History
from models.user import User
from models.store import Store
from models.queue import Queue
import datetime
from app import socketio

history_api_blueprint = Blueprint('history_api',
                             __name__,
                             template_folder='templates')


def call_store():
    stores = Store.select()
    list_of_stores = []
    for store in stores:
        list_of_stores.append(
        {
<<<<<<< HEAD
            "id": store.id,
=======
            "id":store.id,
>>>>>>> ec507ae26c5bb9f5fd8ee5291d1299e58328ff46
            "name":store.name,
            "location":store.location,
            "customer_limit":store.customer_limit,
            "headcount":store.headcount,
            "queue":store.queue
        })
    socketio.emit('store', (list_of_stores))


@history_api_blueprint.route('/<user_id>/user/<store_id>/store', methods=['POST']) #TAKE IN  USER_ID AND STORE_ID TO STORE FOREIGN KEYS ONTO THE NEW HISTORY ENTRY.
<<<<<<< HEAD
# @jwt_required
=======
@jwt_required
>>>>>>> ec507ae26c5bb9f5fd8ee5291d1299e58328ff46
def create(user_id, store_id):

    #GET USER AND STORE FIRST BEFORE PASSING TO NEW_HISTORY.
    user= User.get_or_none(User.id == user_id)
    store = Store.get_or_none(Store.id == store_id)
    history = History.get_or_none((History.user_id == user.id) & (History.time_out == None) ) #VALIDATION, IF USER NOT CHECKEDOUT, PREVENT NEW HISTORY
    queue = Queue.get_or_none(Queue.user_id == user.id)
    queue_exists = Queue.get_or_none(Queue.store_id == store.id)
    store_space = int(store.customer_limit - store.headcount)

    #STORE FULL
    if store.headcount == store.customer_limit: #checks if store limit is reached

        if queue:
            return jsonify({"error":"Shop is full."}) #KIV
        else:
            new_queue = Queue(
                user=user,
                store=store
            )

            if new_queue.save():
                store.queue = store.queue + 1
                store.save()
                call_store()

                return jsonify({
                    "type":"queue",
                    "user":new_queue.user.name,
                    "store":new_queue.store.name
                })
            else:
                return jsonify([err for err in new_history.errors])
   
   #SPACE AVAILABLE, QUEUE EXISTS.
    elif store.headcount < store.customer_limit and queue_exists: #CHECKS IF THERE IS A QUEUE, 

        if queue: #CHECK IF USER IN QUEUE AND QUEUE NUMBER REACHED. CHECK IN USER
            queue_array =[]
            store_queue = Queue.select().where(Queue.store_id == store.id).limit(store_space) #Change limit to store_space
            for q in store_queue:
                queue_array.append(q.user_id) #add user_id into queue array
         
            if queue.user_id in queue_array: 
                queue.delete_instance()
                socketio.emit("queue_update", "queue has been updated")

                new_history = History(
                user = user,
                store = store
                )

                if new_history.save():
                    store.headcount += 1 #STORE HEADCOUNT +1
                    store.queue -= 1
                    store.save()
                    call_store()

                    return jsonify({
                        "id":new_history.id,
                        "user":new_history.user.name,
                        "store":new_history.store.name,
                        "headcount":new_history.store.headcount
                        })
                else:
                    return jsonify([err for err in new_history.errors])
            else:
                return jsonify({"msg":"Not your turn yet. Please come back later."})

        else:
            new_queue = Queue(
                user=user,
                store=store
                )

            if new_queue.save():
                store.queue += 1
                store.save()
                call_store()
                return jsonify({
                    "id":new_queue.id,
                    "type":"queue",
                    "id":new_queue.id,
                    "user":new_queue.user.name,
                    "store":new_queue.store.name
                })
            else:
                return jsonify([err for err in new_history.errors])


    else:
        
        if history: #QUERY OF HISTORY EXISTS, RETURN ERROR.
            return jsonify({"error":"User is not checked out from previous store."})
        else:
            new_history = History(
            user = user,
            store = store
            )

            if new_history.save():
                store.headcount = store.headcount + 1 #STORE HEADCOUNT +1
                store.save()
                call_store()
                return jsonify({
                    "id": new_history.id,
                    "user":new_history.user.name,
                    "store":new_history.store.name,
                    "headcount":new_history.store.headcount
                    })
            else:
                return jsonify([err for err in new_history.errors])
  
        
#CHECKOUT FUNCTION, UPDATE HISTORY.TIME_OUT AND DECREASE STORE HEADCOUNT
@history_api_blueprint.route('/<user_id>/user/<store_id>/store/update', methods=['POST']) 
@jwt_required
def update(user_id, store_id):

    store = Store.get_by_id(store_id)

    history = History.get_or_none(
        (History.user_id == user_id) & 
        (History.store_id == store_id) & 
        (History.time_out == None) #QUERY WHERE USER AND TIME_OUT IS NONE TO MAKE SURE WE GET THE RIGHT HISTORY QUERY.
        )

    history.time_out = datetime.datetime.now() #UPDATE TIME_OUT

    if history.save():
        store.headcount = store.headcount - 1 #Reduce headcount
        store.save()
        call_store()
        
        return jsonify({
            "id":history.id,
            "time_out":history.time_out,
            "user":history.user.name,
            "store":history.store.name,
            "headcount":history.store.headcount
            })
    else:
        return jsonify([err for err in new_history.errors])

@history_api_blueprint.route('/<user_id>/user/all', methods=['GET']) 
@jwt_required
def all_history(user_id):

    histories = History.select().where(History.user_id == user_id)

    call_store()

    list_of_history = []        
    for history in histories:
        list_of_history.append(
        {
            "id":history.id,
            "name":history.store.name,
            "location":history.store.location,
            "time_in":history.time_in,
            "time_out":history.time_out
        })
    return jsonify(list_of_history)


        