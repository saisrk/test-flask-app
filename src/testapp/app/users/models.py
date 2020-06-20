from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from testapp import db
from testapp.common.db import TimestampMixin
from testapp.app.session.models import Attendance, Session
from testapp.app.sadhana_sheet.models import UserSadhana


class User(TimestampMixin, UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    slug = db.Column(db.String(80), unique=True, nullable=False)
    pseudoname = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    hashed_password = db.Column(db.String(120), nullable=False)
    is_bhajan_vikas = db.Column(db.Boolean, default=False)
    phone_number = db.Column(db.String(120), unique=True, nullable=True)
    admin = db.Column(db.Boolean, default=False)
    authenticated = db.Column(db.Boolean, default=False)
    samithi_id = db.Column(db.Integer, db.ForeignKey('samithi.id'), nullable=True)
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_types.id'), nullable=False)
    user_type = db.relationship('Usertype', backref=db.backref('users', lazy=True))
    samithi = db.relationship('Samithi', backref=db.backref('users', lazy=True))
    attendances = db.relationship('Attendance', backref=db.backref('users', lazy=True))
    user_sadhana = db.relationship('UserSadhana', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.username

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'phone_number': self.phone_number,
            'samithi_id': self.samithi_id,
            'username': self.username,
            'email': self.email,
            'user_type_id': self.user_type_id
        }

    def is_active(self):
        return True

    def is_authenticated(self):
        return self.is_authenticated

    def is_anonymous(self):
        return False

    def is_admin(self):
        return self.admin

    def get_id(self):
        return self.id

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


class Usertype(db.Model):
    __tablename__ = 'user_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    slug = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Usertype %r>' % self.name


class Samithi(db.Model):
    __tablename__ = 'samithi'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    slug = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Usertype %r>' % self.name

