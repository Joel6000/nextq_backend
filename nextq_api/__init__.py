from app import app
from flask_cors import CORS

cors = CORS(app, resources={r"*": {"origins": "*"}}) # Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.

## API Routes ##
from nextq_api.blueprints.users.views import users_api_blueprint
from nextq_api.blueprints.stores.views import stores_api_blueprint
from nextq_api.blueprints.history.views import history_api_blueprint
from nextq_api.blueprints.auth.views import auth_api_blueprint
from nextq_api.blueprints.queue.views import queue_api_blueprint



app.register_blueprint(users_api_blueprint, url_prefix='/api/v1/users')
app.register_blueprint(stores_api_blueprint, url_prefix='/api/v1/stores')
app.register_blueprint(history_api_blueprint, url_prefix='/api/v1/history')
app.register_blueprint(auth_api_blueprint, url_prefix='/api/v1/auth')
app.register_blueprint(queue_api_blueprint, url_prefix='/api/v1/queue')