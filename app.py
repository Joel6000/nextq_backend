import os
import peeweedbevolve
import config
from flask import Flask, flash, render_template, request, redirect, url_for, jsonify
from flask_jwt_extended import JWTManager
from database import db

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
jwt = JWTManager(app)


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