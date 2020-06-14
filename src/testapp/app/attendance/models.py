from sqlalchemy_utils import URLType

from testapp import db


class Attendance(db.Model):
    __tablename__ = 'attendance'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=False)
    status = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return '<Attendance %r>' % self.status


class Session(db.Model):
    __tablename__ = 'session'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    slug = db.Column(db.String(80), unique=True, nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    url = db.Column(URLType, nullable=False)
    summary = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self):
        return '<Session %r>' % self.name