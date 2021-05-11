"""app pkg."""

from os import remove

from flask import Flask
from larsmod.file_manager import list_files as get_files


def cleanup():
    "cleanup upload folder"

    print("Cleaning up folder...")
    for file in get_files(app.config["UPLOAD_FOLDER"])[1]:
        remove(file)
    print("Cleanup completed!")

class FlaskClient(Flask):
    """Creates web client instance."""

    def __del__(self):
        "cleanup folder when server closed"

        cleanup()


app = FlaskClient(__name__)
app.config["UPLOAD_FOLDER"] = "web_storage/saved_data"

from web_storage import routes
