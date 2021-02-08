import os
import config
from flask import Flask, flash, render_template, request, redirect, url_for, jsonify
from flask_jwt_extended import JWTManager
from database import db
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
jwt = JWTManager(app)
socketio = SocketIO(app, cors_allowed_origins="*")



if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

@app.before_request
def before_request():
    db.connect()

@app.after_request
def after_request(response):
    db.close()
    return response

@app.route("/") # Revisit decorators if you unclear of this syntax
def index():
    return render_template('index.html')


#TESTING TARGETTED HEADCOUNT

# @socketio.on('targetHeadcount')
# def get_headcount(store_id):
#     from models.store import Store
#     store = Store.get_by_id(store_id)
#     emit('headcount',{"headcount":store.headcount})

# From API (history, checkin) , emit (headcount_queue) from backend to frontend
# socket.on(headcount_queue) emit callStore #from FE to BE
# socket.on(callStore), run function, emit (store,msg) BE TO FE
# socket.on(store), run function, console.log(msg) frontend shows message