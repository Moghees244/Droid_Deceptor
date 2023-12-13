from . import db
import re
from sqlalchemy import Column, String, event
from sqlalchemy.orm import validates, relationship
from sqlalchemy.exc import IntegrityError
import bcrypt


class User(db.Model):
    __tablename__ = 'users'

    name = db.Column(db.String(255), nullable = False)
    username = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    @validates('name')
    def validate_name(self, key, name):
        assert 1 <= len(name) <= 50, "Name must be between 1 and 50 characters"
        assert all(char.isalpha() or char.isspace() for char in name), "Name must contain only letters and spaces"
        return name
    
    @validates('username')
    def validate_username(self, key, username):
        assert 1 <= len(username) <= 50, "Name must be between 1 and 50 characters"
        assert all(char.isalnum() for char in username), "Username must contain only letters, numbers"
        return username

    @validates('email')
    def validate_email(self, key, email):
        email_pattern = re.compile(r'^[a-zA-Z][a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        # Use assert to check if the email is valid
        assert email_pattern.match(email), "Invalid email format"
        return email

    @validates('password')
    def validate_password(self, key, password):
        assert len(password) >= 8, "Password must be at least 8 characters"
        return password

@event.listens_for(User, 'before_insert')
def before_insert_listener(mapper, connection, target):
    salt = bcrypt.gensalt(10)
    hashed_password = bcrypt.hashpw(target.password.encode('utf-8'), salt)
    target.password = hashed_password.decode('utf-8')


def add_user(name, username, email, password):
    try:
        user = User(name=name, username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return {"success": True, "message": "User created successfully."}
    
    except IntegrityError:
        db.session.rollback()
        return {"success": False, "message": "User with this username or email already exists."}
    
    except Exception as e:
        db.session.rollback()
        return {"success": False, "message": f"An error occurred: {str(e)}"}

def remove_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()

def show_user_by_username(username):
    return User.query.filter_by(username=username).first()

def show_all_users():
    return User.query.all()

def verify_login(username, password):
    user = User.query.filter_by(username=username).first()

    # Check if the user exists and the password is correct
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return user
    else:
        return None