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
        image_url=params.get("image_url")
        )

    if new_store.save():
        return jsonify({"storeName":new_store.name,
                        "storeLocation":new_store.location,
                        "image_url":new_store.image_url
                    })
    else:
        return jsonify([err for err in new_store.errors])
        
#GET STORE ID INFORMATION
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


#GET ALL STORE INFORMATION
@stores_api_blueprint.route('/all', methods=['GET'])
def get_all_stores():
    stores = Store.select()
    if stores:
        list_of_stores = []
        
        for store in stores:
            list_of_stores.append(
            {
                "id": store.id,
                "name":store.name,
                "location":store.location,
                "customer_limit":store.customer_limit,
                "headcount":store.headcount,
                "queue":store.queue
            })
        return jsonify(list_of_stores)
        
    else:
        return jsonify([err for err in new_store.errors])


