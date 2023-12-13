from flask import request, redirect, url_for
from flask_jwt_extended import get_jwt_identity, jwt_required
from droid_deceptor.models.feedback import add_feedback

@jwt_required()
def save_feedback():
    if request.method == 'POST':
        hash = request.form['hash']
        feedback = request.form['feedback']
        name = request.form['name']

    #Create a new user
    res = add_feedback(username= get_jwt_identity(), apk_hash=hash, feedback_text=feedback)

    if 'success' in res and res['success']:
        return redirect(url_for('user.display_results', uploaded_file=name, status_message="Feedback Submitted Successfully!"))
    
    return redirect(url_for('user.display_results', uploaded_file=name, status_message="Feedback Not Submitted!"))
