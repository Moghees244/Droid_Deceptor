from flask import Flask
from flask_jwt_extended import JWTManager
from droid_deceptor.config import Config
from droid_deceptor.models import db
from droid_deceptor.routes.auth_routes import auth_routes
from droid_deceptor.routes.user_routes import user_routes
from droid_deceptor.routes.admin_routes import admin_routes


def create_app():
    app = Flask(__name__, static_folder='public')
    jwt = JWTManager(app)
    
    app.config.from_object(Config)
    db.init_app(app)

    app.register_blueprint(auth_routes)
    app.register_blueprint(user_routes)
    app.register_blueprint(admin_routes)

    return app