from . import db
from sqlalchemy import Column, String, event
from sqlalchemy.orm import validates
import bcrypt


class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    @validates('name')
    def validate_name(self, key, name):
        assert 1 <= len(name) <= 50, "Name must be between 1 and 50 characters"
        return name

    @validates('username')
    def validate_username(self, key, username):
        assert 1 <= len(username) <= 50, "Username must be between 1 and 50 characters"
        return username

    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email and '.' in email, "Invalid email format"
        return email

    @validates('password')
    def validate_password(self, key, password):
        assert len(password) >= 6, "Password must be at least 6 characters"
        return password

@event.listens_for(Admin, 'before_insert')
def before_insert_listener(mapper, connection, target):
    salt = bcrypt.gensalt(10)
    hashed_password = bcrypt.hashpw(target.password.encode('utf-8'), salt)
    target.password = hashed_password.decode('utf-8')


def add_admin(name, username, email, password):
    admin = Admin(name=name, username=username, email=email, password=password)
    db.session.add(admin)
    db.session.commit()

def remove_admin(admin_id):
    admin = Admin.query.get(admin_id)
    if admin:
        db.session.delete(admin)
        db.session.commit()

def show_admin_by_username(username):
    return Admin.query.filter_by(username=username).first()

def show_all_admins():
    return Admin.query.all()
