from flask import Blueprint
from droid_deceptor.controllers.apk_upload import upload_apk
from droid_deceptor.controllers.feature_extractor import display_results

user_routes = Blueprint('blueprint', __name__)
user_routes.route('/upload', methods=['POST', 'GET'])(upload_apk)
user_routes.route('/results', methods=['POST', 'GET'])(display_results)