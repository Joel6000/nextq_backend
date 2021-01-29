import os
import peeweedbevolve
import config
from flask import Flask, flash, render_template, request, redirect, url_for, jsonify
from flask_jwt_extended import create_access_token

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

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

if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
   app.run()