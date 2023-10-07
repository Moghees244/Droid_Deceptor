import os
from flask import render_template
from droid_deceptor.controllers.feature_extractor import extract_features

def get_apk(files):
    UPLOAD_FOLDER = 'droid_deceptor/uploads'

    success_message, error_message , uploaded_file = None, None, None

    # Check if the 'file' field is in the request
    if 'file' not in files:
        error_message = "No file Uploaded"

    file = files['file']

    # Check if the user submitted an empty file input
    if file.filename == '':
        error_message = "No selected file"

    if file:
        # Ensure the folder exists
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        # Save the uploaded APK file to the UPLOAD_FOLDER
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        uploaded_file = file.filename
        success_message = "File Saved"

        # extract features
        features = extract_features(file.filename)

    return render_template('upload.html', success_message=success_message, error_message=error_message, uploaded_file=uploaded_file, features=features)