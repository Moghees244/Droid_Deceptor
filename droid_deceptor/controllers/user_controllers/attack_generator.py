import json
from flask import render_template, request, jsonify
from flask_jwt_extended import jwt_required
from droid_deceptor.controllers.user_controllers.attacks import Attacks
import droid_deceptor.controllers.user_controllers.malware_classification as models
from droid_deceptor.controllers.user_controllers.feature_extractor import prepare_input, malware_classifier

@jwt_required()
def generate_attack():
    if request.method == 'GET':
        return "Method Not Allowed"
    
    features_json = request.form['features']
    # Fix JSON formatting if necessary
    features_json_fixed = features_json.replace("'", '"')
        
        # Parse the JSON data
    try:
        features = json.loads(features_json_fixed)
    except json.decoder.JSONDecodeError as e:
        return f"Error decoding JSON: {e}"

    attack = Attacks()
    attack.model = models.svm_classifier
    attack.apk_vector = prepare_input(features)

    adversarial_vector = attack.jsma_attack(10)
    perturbations = attack.features_names(adversarial_vector)
    classification = malware_classifier(adversarial_vector)

    return render_template('attack.html', features=perturbations, classification=classification)