from flask import Flask, request, render_template
from droid_deceptor.controllers.apk_upload import get_apk

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def upload_apk():
    if request.method == "POST":
        return get_apk(request.files)

    # Render the 'upload.html' template for the 'GET' request
    return render_template('upload.html')