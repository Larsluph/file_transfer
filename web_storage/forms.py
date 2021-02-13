"""contains forms used in app."""

from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField, FileField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    """Login form."""

    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(4, 32)
    ])
    submit = SubmitField("Login")


class UploadForm(FlaskForm):
    """Form to upload file to server."""

    file = FileField('file')
    submit = SubmitField('submit')
