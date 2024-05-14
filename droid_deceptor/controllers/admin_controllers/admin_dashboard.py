from flask_jwt_extended import jwt_required, get_jwt_identity
from droid_deceptor.models.admin import show_admin_by_username
from droid_deceptor.models.feedback import get_all_feedbacks
from droid_deceptor.models.admin import show_all_admins
from droid_deceptor.models.user import show_all_users
from droid_deceptor.models.apk import show_all_apks
from flask import render_template

@jwt_required()
def dashboard():
    
    current_user = get_jwt_identity()

    if show_admin_by_username(current_user) != None:
        return render_template('admin_dashboard.html', feedbacks = get_all_feedbacks(), admins=show_all_admins(), users=show_all_users(), apks=show_all_apks())
    
    return render_template('error401.html')