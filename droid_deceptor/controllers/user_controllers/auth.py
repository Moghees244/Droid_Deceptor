from flask import render_template, request, redirect, url_for, flash
from models.user import User
from droid_deceptor import db

def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if the username or email already exists
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            flash('Username or email already exists. Please choose a different one.', 'error')
            return redirect(url_for('signup'))

        # Create a new user
        new_user = User(username=username, email=email, password=password)

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully. You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')


def login():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if the username or email already exists
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            flash('Username or email already exists. Please choose a different one.', 'error')
            return redirect(url_for('signup'))

        # Create a new user
        new_user = User(username=username, email=email, password=password)

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully. You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

