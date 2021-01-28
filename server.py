from flask import Flask
app = Flask(__name__)

@app.route("/") # Revisit decorators if you unclear of this syntax
def index():
    return '<h1>Why so easy</h1>'

@app.before_request
def before_request():
    db.connect()

@app.after_request
def after_request(response):
    db.close()
    return response



if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
   app.run()