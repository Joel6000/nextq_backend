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


@queue_api_blueprint.route('/<user_id>/user/<store_id>/store', methods=['POST'])
def create(user_id, store_id):
    pass
