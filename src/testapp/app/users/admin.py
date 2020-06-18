from flask import Blueprint
from flask_admin.contrib.sqla import ModelView

from testapp import db, admin
from testapp.app.users.models import User

users_admin = Blueprint('users_admin', __name__)

admin.add_view(ModelView(User, db.session))