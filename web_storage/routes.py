"""Contains routes used in main app."""


from datetime import datetime
from os.path import join as join_path
from os.path import exists as is_exists

import flask
from larsmod.file_manager import list_files as get_files
from werkzeug.utils import secure_filename

from web_storage import app, cleanup


@app.route('/')
def home_page():
    return flask.render_template("home.html")

@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if flask.request.method == 'POST':
        if 'files' in flask.request.files:
            files = flask.request.files.getlist('files')
            print(f"got {len(files)} files")

            for file in files:
                if file.filename != "":
                    filename = secure_filename(file.filename)
                    print(file.filename, filename)
                    if is_exists(join_path(app.config["UPLOAD_FOLDER"], filename)):
                        i = filename.rfind('.')
                        filename = f"{filename[:i]}_copy{filename[i:]}"
                        print(f"renamed: {filename}")
                    file.save(join_path(app.config["UPLOAD_FOLDER"], filename))
                    print(f'file "{filename}" saved')

    return flask.render_template("upload.html")

@app.route("/uploaded/<path:filename>")
def uploaded_file(filename):
    return flask.send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route("/listfiles")
def list_files():
    files = get_files(dirpath=app.config["UPLOAD_FOLDER"])[1]

    return flask.render_template("listfiles.html", filelist=map(lambda x: x.split("\\")[-1], files))

@app.route("/cleanup")
def clear_dir():
    cleanup()
    return "<h2>Server storage cleaned up!</h2>"
