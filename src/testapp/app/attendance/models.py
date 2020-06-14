from testapp import db
from testapp.app.users.models import User


class Attendance(db.Model):
    __tablename__ = 'attendance'


class Session(db.Model):
    __tablename__ = 'session'