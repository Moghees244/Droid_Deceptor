from flask import Blueprint
from droid_deceptor.controllers.user_controllers.user_auth import login, signup
from droid_deceptor.controllers.admin_controllers.admin_auth import admin_login, admin_signup

auth_routes = Blueprint('auth', __name__)

auth_routes.route('/login', methods=['POST', 'GET'])(login)
auth_routes.route('/signup', methods=['POST', 'GET'])(signup)

auth_routes.route('/admin/login', methods=['POST', 'GET'])(admin_login)
auth_routes.route('/admin/signup', methods=['POST', 'GET'])(admin_signup)