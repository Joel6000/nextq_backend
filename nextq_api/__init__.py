from app import app
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##
from nextq_api.blueprints.users.views import users_api_blueprint

app.register_blueprint(nextq_api_blueprint, url_prefix='/api/nextq/users')