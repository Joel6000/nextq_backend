from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from models.shop import Shop

shops_api_blueprint = Blueprint('shops_api',
                             __name__,
                             template_folder='templates')

#SHOP API DRAFT
@shops_api_blueprint.route('/new', methods=['POST'])
def new_shop():
    params = request.json
    new_shop = Shop(
        name = params.get("name"), 
        limit=params.get("limit")
        )

    if new_shop.save():
        token = create_access_token(identity = new_shop.id) #somehting else here
        return jsonify({"token":token})
    else:
        return jsonify([err for err in new_shop.errors])