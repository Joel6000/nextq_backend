from app import app
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##
from nextq_api.blueprints.users.views import users_api_blueprint
from nextq_api.blueprints.shops.views import shops_api_blueprint


app.register_blueprint(users_api_blueprint, url_prefix='/api/nextq/users')
app.register_blueprint(shops_api_blueprint, url_prefix='/api/nextq/shops')