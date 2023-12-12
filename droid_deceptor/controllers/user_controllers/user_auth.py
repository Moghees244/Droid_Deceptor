from datetime import timedelta
from flask import render_template, request, redirect, url_for, jsonify
from flask_jwt_extended import create_access_token, set_access_cookies, verify_jwt_in_request, unset_jwt_cookies, get_jwt
from droid_deceptor.models.user import add_user, verify_login

def signup():
    res = None

    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        #Create a new user
        res = add_user(name=name, username=username, email=email, password=password)

        if 'success' in res and res['success']:
            return redirect(url_for('auth.login'))

    return render_template('user_signup.html', error = res.get('message') if res else None)


def login():
    error_message = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if verify_login(username, password):
            access_token = create_access_token(identity=username, expires_delta=timedelta(days=1))
            # Set the JWT in cookies
            response = redirect(url_for('user.upload_apk'))
            set_access_cookies(response, access_token)

            return response
        else:
            error_message = "Incorrect Credentials."

    if request.method == 'GET':
        access_token = request.cookies.get("access_token_cookie")

        if access_token:
            if verify_jwt_in_request():
                return redirect(url_for('user.upload_apk'))

    return render_template('user_login.html', error = error_message)

def logout():
    response = redirect(url_for('auth.login'))
    unset_jwt_cookies(response)
    return response

