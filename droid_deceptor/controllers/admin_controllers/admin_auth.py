from datetime import timedelta
from flask import render_template, request, redirect, url_for
from flask_jwt_extended import create_access_token, set_access_cookies
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, jwt_required, unset_jwt_cookies
from droid_deceptor.models.admin import verify_login, add_admin, show_admin_by_username

@jwt_required()
def admin_signup():
    res = None

    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        #Create a new admin
        res = add_admin(name=name, username=username, email=email, password=password)
  
        if 'success' in res and res['success']:
            return redirect(url_for('admin.dashboard'))
        
    current_user = get_jwt_identity()
    
    if show_admin_by_username(current_user) != None:
        return render_template('admin_signup.html', error = res.get('message') if res else None)

def admin_login():
    error_message = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if verify_login(username, password):
            access_token = create_access_token(identity=username, expires_delta=timedelta(days=1))
            # Set the JWT in cookies
            response = redirect(url_for('admin.dashboard'))
            set_access_cookies(response, access_token)
            return response    
        else:
            error_message = "Incorrect Credentials."

    if request.method == 'GET':
        access_token = request.cookies.get("access_token_cookie")

        if access_token:
            if verify_jwt_in_request():
                current_user = get_jwt_identity()

                if show_admin_by_username(current_user) != None:
                    return redirect(url_for('admin.dashboard'))

    return render_template('admin_login.html', error = error_message)


def admin_logout():
    response = redirect(url_for('auth.admin_login'))
    unset_jwt_cookies(response)
    return response
