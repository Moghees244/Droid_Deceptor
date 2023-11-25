from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from droid_deceptor.routes.user_routes import user_routes

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:admin@localhost/droid_deceptor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.register_blueprint(user_routes)
