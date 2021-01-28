from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from models.shop import Shop

shops_api_blueprint = Blueprint('shops_api',
                             __name__,
                             template_folder='templates')