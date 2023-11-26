from . import db
from droid_deceptor.models.user import User
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import validates, relationship

class Apk(db.Model):
    __tablename__ = 'apks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    hash = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(50), ForeignKey('users.username'))

    user = relationship('User', back_populates='apks')

    @validates('name')
    def validate_name(self, key, name):
        assert 1 <= len(name) <= 100, "APK name must be between 1 and 100 characters"
        return name
    
    @validates('hash')
    def validate_hash(self, key, hash):
        assert 1 <= len(hash) <= 100, "APK name must be between 1 and 100 characters"
        return hash

# Create a relationship between User and Apk
User.apks = relationship('Apk', back_populates='user')

def add_apk(name, hash, username):
    user = User.query.filter_by(username=username).first()
    if user:
        apk = Apk(name=name, hash=hash, username=username)
        db.session.add(apk)
        db.session.commit()
        return True
    return False

def remove_apk(apk_id):
    apk = Apk.query.get(apk_id)
    if apk:
        db.session.delete(apk)
        db.session.commit()

def show_apk_by_name(name):
    return Apk.query.filter_by(name=name).first()

def show_all_apks():
    return Apk.query.all()