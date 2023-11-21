from flask import Flask
from droid_deceptor.routes.user import user_routes

app = Flask(__name__)
app.register_blueprint(user_routes)
