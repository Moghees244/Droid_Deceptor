import json, os, shutil, subprocess
from droid_deceptor.config import Paths
from flask import render_template, request, send_file
from flask_jwt_extended import jwt_required
from droid_deceptor.controllers.user_controllers.attacks import Attacks
import droid_deceptor.controllers.user_controllers.malware_classification as models
from droid_deceptor.controllers.user_controllers.feature_extractor import prepare_input, malware_classifier

@jwt_required()
def generate_attack():
    if request.method == 'GET':
        return "Method Not Allowed"
    
    name = request.form['name']
    features_json = request.form['features']
    # Fix JSON formatting if necessary
    features_json_fixed = features_json.replace("'", '"')
        
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

    #new_apk = modify_apk(name, perturbations)

    return render_template('attack.html', features=perturbations, classification=classification)


@jwt_required()
def download_file(filename):
    if os.path.exists(filename):
        return send_file(filename, as_attachment=True)
    else:
        return "File not found", 404

def modify_apk(name, features):
    apk_path = os.path.join(Paths.apks_path, name)

    if not os.path.exists(apk_path):
        return f"APK file '{name}' not found."

    # Decompiling APK using apktool
    decompiled_path = os.path.join(Paths.jadx_output_path, 'temp_decompiled_apk')
    if os.path.exists(decompiled_path):
        shutil.rmtree(decompiled_path)
    os.makedirs(decompiled_path)

    try:
        decompile_apk(apk_path, decompiled_path)
        modify_manifest(os.path.join(decompiled_path, "AndroidManifest.xml"), features)
        recompile_apk(decompiled_path, name)
        return os.path.join(Paths.apks_path, f'{name}_modified.apk')
    finally:
        # Clean up decompiled files
        shutil.rmtree(decompiled_path)

def decompile_apk(apk_path, decompiled_path):
    command = f"apktool d -f {apk_path} -o {decompiled_path}"
    print(command)
    subprocess.run(command, shell=True, check=True)

def modify_manifest(manifest_path, features):
    with open(manifest_path, "r") as f:
        manifest_content = f.read()

    for feature in features:
        manifest_content = add_permission_to_manifest(manifest_content, feature)

    with open(manifest_path, "w") as f:
        f.write(manifest_content)

def add_permission_to_manifest(manifest_content, feature):
    if feature.startswith("android.permission") or feature.startswith("android.intent") or feature.startswith("android.hardware"):
        manifest_content = manifest_content.replace("</application>", f"\t<{feature} />\n</application>")
    return manifest_content

def recompile_apk(decompiled_path, name):
    command = f"apktool b {decompiled_path} -o {os.path.join(Paths.apks_path, f'modified.apk')}"
    subprocess.run(command, shell=True, check=True)