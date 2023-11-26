from flask import Blueprint
from droid_deceptor.controllers.auth import login, signup

auth_routes = Blueprint('auth', __name__)

auth_routes.route('/login', methods=['POST', 'GET'])(login)
auth_routes.route('/signup', methods=['POST', 'GET'])(signup)