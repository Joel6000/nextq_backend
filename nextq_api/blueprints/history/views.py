from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required #similar to login_required, a decorator to make sure that JWT token must be present for the function to be called
from models.history import History
from models.user import User
from models.store import Store
from models.queue import Queue
import datetime

history_api_blueprint = Blueprint('history_api',
                             __name__,
                             template_folder='templates')


@history_api_blueprint.route('/<user_id>/user/<store_id>/store', methods=['POST']) #TAKE IN  USER_ID AND STORE_ID TO STORE FOREIGN KEYS ONTO THE NEW HISTORY ENTRY.
def create(user_id, store_id):

    #GET USER AND STORE FIRST BEFORE PASSING TO NEW_HISTORY.
    user= User.get_or_none(User.id == user_id)
    store = Store.get_or_none(Store.id == store_id)
    history = History.get_or_none((History.user_id == user.id) & (History.time_out == None) ) #VALIDATION, IF USER NOT CHECKEDOUT, PREVENT NEW HISTORY
    queue = Queue.get_or_none(Queue.user_id == user.id)

    if store.headcount == store.customer_limit:

        if queue:
            return jsonify({"error":"User already in queue."})
        else:
            new_queue = Queue(
                user=user,
                store=store
            )

            if new_queue.save():
                return jsonify({
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
                return jsonify({
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
    print("before save")
    if history.save():
        store.headcount = store.headcount - 1 #Reduce headcount
        store.save()
        print("after save")
        return jsonify({
            "time_out":history.time_out,
            "user":history.user.name,
            "store":history.store.name,
            "headcount":history.store.headcount
            })
    else:
        return jsonify([err for err in new_history.errors])
