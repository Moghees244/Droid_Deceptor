from flask import Blueprint, redirect, url_for
from droid_deceptor.controllers.admin_controllers.admin_dashboard import dashboard


admin_routes = Blueprint('admin', __name__)

admin_routes.route('/admin/')(lambda: redirect(url_for('auth.admin_login')))
admin_routes.route('/admin/dashboard')(dashboard)