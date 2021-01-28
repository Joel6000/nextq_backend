from flask import Flask, flash, render_template, request, redirect, url_for, jsonify
from flask_jwt_extended import create_access_token
import os
import peeweedbevolve
from models import db
from models import *

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.before_request
def before_request():
    db.connect()

@app.after_request
def after_request(response):
    db.close()
    return response

@app.cli.command()
def migrate():
   db.evolve(ignore_tables={'base_model'})

@app.route("/") # Revisit decorators if you unclear of this syntax
def index():
    return render_template('index.html')

#USER API DRAFT
@app.route('/user/new', methods=['POST'])
def new_user():
    params = request.json
    new_user = User(
        username = params.get("username"), 
        email=params.get("email"), 
        password=params.get("password"),
        mobile_number=params.get("mobilehp")
        )

    if new_user.save():
        token = create_access_token(identity = new_user.id)
        return jsonify({"token":token})
    else:
        return jsonify([err for err in new_user.errors])

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get_or_none(user.id == user_id)

    if user:
        token = create_access_token(identity = user.id)
        return jsonify({"token":token})
    else:
        return jsonify([err for err in new_user.errors])

@app.route('/user/<user_id>/checkin', methods=['POST'])
def user_checkin(user_id):
    user = User.get_or_none(user.id == user_id)

    if user:
        pass
    else:
        pass

#SHOP API DRAFT
@app.route('/shop/new', methods=['POST'])
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

if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
   app.run()