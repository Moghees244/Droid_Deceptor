from . import db
from droid_deceptor.models.user import User
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import validates, relationship

class Feedback(db.Model):
    __tablename__ = 'feedbacks'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    apk_hash = db.Column(db.String(255))
    feedback = db.Column(db.String(255))


    @validates('feedback')
    def validate_feedback(self, key, feedback):
        assert 1 <= len(feedback) <= 255, "Feedback must be between 1 and 255 characters"
        return feedback

def add_feedback(username, apk_hash, feedback_text):
    try:
        # Validate feedback length
        assert 1 <= len(feedback_text) <= 255, "Feedback must be between 1 and 255 characters"

        # Create a new Feedback object
        feedback = Feedback(username=username, apk_hash=apk_hash, feedback=feedback_text)

        # Add the feedback to the database
        db.session.add(feedback)
        db.session.commit()

        return {"success": True, "message": "Feedback added successfully."}

    except AssertionError as e:
        db.session.rollback()
        return {"success": False, "message": str(e)}

    except Exception as e:
        db.session.rollback()
        return {"success": False, "message": f"An error occurred: {str(e)}"}
    

def get_all_feedbacks():
    try:
        feedbacks = Feedback.query.all()
        return feedbacks

    except Exception as e:
        return {"success": False, "message": f"An error occurred: {str(e)}"}

