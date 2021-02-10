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

@socketio.on('get_queue_number')
def get_queue(user_id):
    queue = Queue.get_or_none(Queue.user_id == user_id)
    socketio.emit("queue_number", queue_number) #KIV
    if queue:
        queue_list = Queue.select().where(Queue.store_id == queue.store_id)

        if queue_list:
            queue_number = 0
            for index, user_queue in enumerate(queue_list):
                if user_queue.user_id == queue.user_id:
                    queue_number = index + 1
            socketio.emit("queue_number", queue_number)
        else:
            return 0

    else:
        return 0 

