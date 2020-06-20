from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired

from testapp.app.users.models import Samithi, Usertype


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    samithi = SelectField('email', validators=[DataRequired()])

    def get_samithi_choices(self):
        samithis = Samithi.query.all()
        return [(samithi.name, samithi.slug) for samithi in samithis]
