from flask_jwt_extended import jwt_required, get_jwt_identity
from droid_deceptor.models.admin import show_admin_by_username
from flask import render_template

@jwt_required(locations="cookies")
def dashboard():
    current_user = get_jwt_identity()

    if show_admin_by_username(current_user) != None:
        return render_template('admin_dashboard.html')
    
    return render_template('error401.html')