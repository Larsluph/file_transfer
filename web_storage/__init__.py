"""app pkg."""

from web_storage import routes
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class FlaskClient(Flask):
    """Creates web client instance."""

    pass


app = FlaskClient(__name__)
app.config["IMAGE_UPLOADS"] = r"D:\Dev\Scripts\py\Utilitaires\web_apps\file_storage\web_storage\saved_data"
