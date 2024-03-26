from flask import Blueprint, render_template
from droid_deceptor.controllers.user_controllers.apk_upload import upload_apk
from droid_deceptor.controllers.user_controllers.feature_extractor import display_results
from droid_deceptor.controllers.user_controllers.attack_generator import generate_attack
from droid_deceptor.controllers.user_controllers.feedback import save_feedback

user_routes = Blueprint('user', __name__)

user_routes.route('/')(lambda: render_template('home.html'))
user_routes.route('/upload', methods=['POST', 'GET'])(upload_apk)
user_routes.route('/results', methods=['POST', 'GET'])(display_results)
user_routes.route('/attack', methods=['POST'])(generate_attack)
user_routes.route('/feedback', methods=['POST', 'GET'])(save_feedback)