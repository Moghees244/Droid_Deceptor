import os
from flask import render_template
from droid_deceptor.controllers.feature_extractor import extract_features


def get_apk(files):
    UPLOAD_FOLDER = 'droid_deceptor/uploads'

    message, uploaded_file, features, results, perturbations = None, None, None, None, None

    # Check if the 'file' field is in the request
    if 'file' not in files:
        message = "No file Uploaded"

    file = files['file']

    # Check if the user submitted an empty file input
    if file.filename == '':
        message = "No selected file"

    if file:
        # Ensure the folder exists
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        # Save the uploaded APK file to the UPLOAD_FOLDER
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        uploaded_file = file.filename
        message = "File Saved"

        # extract features
        features = extract_features(file.filename)

    return render_template('upload.html', message=message, uploaded_file=uploaded_file, features=features)