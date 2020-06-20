from flask import Blueprint
from flask_admin.contrib.sqla import ModelView

from testapp import db, admin
from testapp.app.attendance.models import Attendance, Session

attendance_admin = Blueprint('attendance_admin', __name__)

admin.add_view(ModelView(Attendance, db.session))
admin.add_view(ModelView(Session, db.session))