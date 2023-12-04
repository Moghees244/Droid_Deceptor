from . import db
from sqlalchemy import Column, String, event
from sqlalchemy.orm import validates, relationship
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
        return name
    
    @validates('username')
    def validate_username(self, key, username):
        assert 1 <= len(username) <= 50, "Name must be between 1 and 50 characters"
        return username

    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email and '.' in email, "Invalid email format"
        return email

    @validates('password')
    def validate_password(self, key, password):
        assert len(password) >= 6, "Password must be at least 6 characters"
        return password

@event.listens_for(User, 'before_insert')
def before_insert_listener(mapper, connection, target):
    salt = bcrypt.gensalt(10)
    hashed_password = bcrypt.hashpw(target.password.encode('utf-8'), salt)
    target.password = hashed_password.decode('utf-8')


def add_user(name, username, email, password):
    user = User(name=name, username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()

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