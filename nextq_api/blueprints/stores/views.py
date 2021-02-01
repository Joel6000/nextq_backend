from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from models.store import Store

stores_api_blueprint = Blueprint('stores_api',
                             __name__,
                             template_folder='templates')

#SHOP API DRAFT
@stores_api_blueprint.route('/new', methods=['POST'])
def new_store():
    params = request.json
    new_store = Store(
        name = params.get("name"),
        location = params.get("location"), 
        customer_limit=params.get("limit")
        )

    if new_store.save():
        return jsonify({"name":new_store.name})
    else:
        return jsonify([err for err in new_store.errors])