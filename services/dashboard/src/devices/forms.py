from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DeviceForm(FlaskForm):
    name = StringField("Device Name", validators=[DataRequired()])
    make = StringField("Device Make", validators=[DataRequired()])
    model = StringField("Device Model", validators=[DataRequired()])
    submit = SubmitField("Post")
