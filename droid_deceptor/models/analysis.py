from . import db
from droid_deceptor.models.apk import Apk
from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY
from sqlalchemy.orm import validates, relationship

class Analysis(db.Model):
    __tablename__ = 'analysis'

    id = db.Column(db.Integer, primary_key=True)
    features = db.Column(ARRAY(String(50)))
    classes = db.Column(ARRAY(String(50)))
    apk_id = db.Column(db.Integer, ForeignKey('apks.id'))
    apk = relationship('Apk', back_populates='analyses')

    @validates('features')
    def validate_features(self, key, features):
        assert all(1 <= len(feature) <= 50 for feature in features), "Feature names must be between 1 and 50 characters"
        return features

    @validates('classes')
    def validate_classes(self, key, classes):
        assert all(1 <= len(cls) <= 50 for cls in classes), "Class names must be between 1 and 50 characters"
        return classes

def add_analysis(features, classes, apk_id):
    analysis = Analysis(features=features, classes=classes, apk_id=apk_id)
    db.session.add(analysis)
    db.session.commit()

def delete_analysis(analysis_id):
    analysis = Analysis.query.get(analysis_id)
    if analysis:
        db.session.delete(analysis)
        db.session.commit()

def search_analysis_by_apk_id(apk_id):
    return Analysis.query.filter_by(apk_id=apk_id).all()

def search_analysis_by_apk_name(apk_name):
    apk = Apk.query.filter_by(name=apk_name).first()
    if apk:
        return Analysis.query.filter_by(apk_id=apk.id).all()
    return []
