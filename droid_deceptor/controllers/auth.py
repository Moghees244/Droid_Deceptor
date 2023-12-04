from flask import render_template, request, redirect, url_for, flash
from droid_deceptor.models.user import add_user, verify_login

def signup():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        #Create a new user
        add_user(name=name, username=username, email=email, password=password)
  
        flash('Account created successfully. You can now log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('signup.html')


def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if verify_login(username, password):
            return redirect(url_for('user.upload_apk'))

    return render_template('login.html')
