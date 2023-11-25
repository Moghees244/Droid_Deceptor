from flask import Blueprint
from droid_deceptor.controllers.user_controllers.auth import login, signup
from droid_deceptor.controllers.user_controllers.apk_upload import upload_apk
from droid_deceptor.controllers.user_controllers.feature_extractor import display_results

user_routes = Blueprint('user', __name__)

user_routes.route('/', methods=['POST', 'GET'])(login)
user_routes.route('/signup', methods=['POST', 'GET'])(signup)
user_routes.route('/upload', methods=['POST', 'GET'])(upload_apk)
user_routes.route('/results', methods=['POST', 'GET'])(display_results)