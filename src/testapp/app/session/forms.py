from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, DateField, TimeField, TextAreaField
from wtforms.validators import DataRequired


class SessionForm(FlaskForm):
    name = StringField('Session Name', validators=[DataRequired()])
    date = DateField('Session Date', validators=[DataRequired()])
    start_time = TimeField('Session Start time', validators=[DataRequired()])
    end_time = TimeField('Session End Time', validators=[DataRequired()])
    session_url = StringField('Session URL', validators=[DataRequired()])
    summary = TextAreaField('Summary')
