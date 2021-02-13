"""Contains routes used in main app."""

import os
import flask
from datetime import datetime
from werkzeug.utils import secure_filename

from web_storage import app
from web_storage.forms import LoginForm, UploadForm


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if flask.request.method == 'POST':
        if flask.request.files:
            file = flask.request.files['file']

            if file.filename == "":
                print("no filename")
            else:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
                print("image saved")

            return flask.redirect(flask.request.url)

    return flask.render_template("upload.html", form=UploadForm)
