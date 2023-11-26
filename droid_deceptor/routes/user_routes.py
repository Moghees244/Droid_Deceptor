from flask import Blueprint
from droid_deceptor.controllers.user_controllers.apk_upload import upload_apk
from droid_deceptor.controllers.user_controllers.feature_extractor import display_results

user_routes = Blueprint('user', __name__)

user_routes.route('/upload', methods=['POST', 'GET'])(upload_apk)
user_routes.route('/results', methods=['POST', 'GET'])(display_results)