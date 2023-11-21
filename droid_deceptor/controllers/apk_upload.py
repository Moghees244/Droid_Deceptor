import os
from flask import render_template
from droid_deceptor.controllers.feature_extractor import extract_features
import droid_deceptor.controllers.malware_classification as Classifiers
from droid_deceptor.controllers.attacks import Attacks


def generate_attack(features, results):
    attack = Attacks()

    attack.model = Classifiers.svm_classifier
    attack.apk_vector = features

    adversarial_example = attack.jsma_attack(max_perturbations= 10)
    perturbations = attack.features_names(adversarial_example)
    return perturbations


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
        apk_vector = Classifiers.prepare_input(features)

        # check if its a malware or not
        results = Classifiers.malware_classifier(apk_vector)
        perturbations = generate_attack(apk_vector, results)

    return render_template('upload.html', message=message, uploaded_file=uploaded_file, features=features, results=results, perturbations=perturbations)