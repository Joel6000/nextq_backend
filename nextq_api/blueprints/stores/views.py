from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from models.store import Store
from app import socketio

stores_api_blueprint = Blueprint('stores_api',
                             __name__,
                             template_folder='templates')

#STORE CREATE API
@stores_api_blueprint.route('/new', methods=['POST'])
def create():
    params = request.json
    new_store = Store(
        name = params.get("name"),
        location= params.get("location"),
        customer_limit= params.get("limit"),
        )

    if new_store.save():
        return jsonify({"storeName":new_store.name,
                        "storeLocation":new_store.location
                    })
    else:
        return jsonify([err for err in new_store.errors])
        
#GET STORE INFORMATION
@stores_api_blueprint.route('/<store_id>/', methods=['GET'])
def get_store(store_id):
    store = Store.get_by_id(store_id)
    if store:
        return jsonify({
            "name":store.name,
            "location":store.location,
            "customer_limit":store.customer_limit,
            "headcount":store.headcount,
            "queue":store.queue
        })
    else:
        return jsonify([err for err in new_store.errors])