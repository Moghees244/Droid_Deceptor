from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from werkzeug.exceptions import Unauthorized
from .config import Config
from .models import db
from .routes.auth_routes import auth_routes
from .routes.error_routes import error_routes
from .routes.user_routes import user_routes
from .routes.admin_routes import admin_routes


def create_app():
    app = Flask(__name__, static_folder='public')
    jwt = JWTManager(app)
    
    app.config.from_object(Config)
    db.init_app(app)
    
    app.register_blueprint(auth_routes)
    app.register_blueprint(error_routes)
    app.register_blueprint(user_routes)
    app.register_blueprint(admin_routes)

    return app