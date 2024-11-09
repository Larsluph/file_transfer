"""app pkg"""
import secrets
from os import remove, getcwd
from os.path import basename as get_filename, join
from os.path import exists as is_exists
from os.path import join as join_path
from os.path import splitext

from flask import Flask, render_template, request, send_from_directory, session
from flask_oidc import OpenIDConnect
from larsmod.file_manager import list_files as get_files
from werkzeug.utils import secure_filename

from .assoc import *
from .oidc_utils import require_admin


def get_ext(x): return splitext(x)[1]


def cleanup():
    """cleanup upload folder"""

    print("Cleaning up folder...")
    for file in get_files(app.config["UPLOAD_FOLDER"])[1]:
        remove(file)
    print("Cleanup completed!")


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = join(getcwd(), "web_storage", "saved_data")
app.config["SECRET_KEY"] = secrets.token_urlsafe(64)
app.config["OIDC_CLIENT_SECRETS"] = join(getcwd(), "web_storage", "config", "client_secrets.json")
app.config["OIDC_SCOPES"] = "openid profile email"

oidc = OpenIDConnect(app)


@app.route('/')
def home_page():
    return render_template("home.html")


@app.route("/upload", methods=["GET", "POST"])
@oidc.require_login
def upload_file():
    if request.method == 'POST':
        if 'files' in request.files:
            files = request.files.getlist('files')
            print(f"got {len(files)} files")

            for file in files:
                if file.filename != "":
                    filename = secure_filename(file.filename)
                    if is_exists(join_path(app.config["UPLOAD_FOLDER"], filename)):
                        i = filename.rfind('.')
                        filename = f"{filename[:i]}_copy{filename[i:]}"
                    file.save(join_path(app.config["UPLOAD_FOLDER"], filename))
                    print(f'file "{filename}" saved')

    return render_template("upload.html")


@app.route("/uploaded/<path:filename>")
@oidc.require_login
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


@app.route("/listfiles")
@oidc.require_login
def list_files():
    files = get_files(dirpath=app.config["UPLOAD_FOLDER"])[1]
    file_list = list(map(get_filename, files))
    classes = list(map(lambda x: collections.get(get_ext(x)[1:], UNKNOWN), file_list))

    return render_template("listfiles.html", filelist=zip(file_list, classes))


@app.route("/cleanup")
@oidc.require_login
def clear_dir():
    cleanup()
    return """<h2>Server storage cleaned up!</h2>
<script>
setTimeout(function () {
  window.location.href = "/upload";
}, 2000);
</script>"""


@app.route('/current_user')
@oidc.require_login
@require_admin
def current_user():
    return session["oidc_auth_profile"]
