from flask import render_template, request, redirect, url_for, flash
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
            return redirect(url_for('user.upload_apk'))
        else:
            error_message = "Incorrect Credentials."

    return render_template('user_login.html', error = error_message)
