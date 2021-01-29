from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from models import Store

stores_api_blueprint = Blueprint('stores_api',
                             __name__,
                             template_folder='templates')

#SHOP API DRAFT
@stores_api_blueprint.route('/new', methods=['POST'])
def new_shop():
    params = request.json
    new_store = Store(
        name = params.get("name"), 
        customer_limit=params.get("limit")
        )

    if new_store.save():
        token = create_access_token(identity = new_store.id) #somehting else here
        return jsonify({"token":token})
    else:
        return jsonify([err for err in new_store.errors])