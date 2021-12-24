"""app pkg."""

import os

from flask import Flask
from larsmod.file_manager import list_files as get_files


def cleanup():
    "cleanup upload folder"

    print("Cleaning up folder...")
    for file in get_files(app.config["UPLOAD_FOLDER"])[1]:
        os.remove(file)
    print("Cleanup completed!")


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = os.path.join(os.getcwd(), "web_storage", "saved_data")

from web_storage import routes
