from flask import Blueprint, render_template

error_routes = Blueprint('error', __name__)

@error_routes.route('/<path:path>')
def handle_error(path):
    return render_template('error404.html')

@error_routes.route('/error-401')
def unauthorized_error():
    return render_template('error401.html')