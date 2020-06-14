from datetime import datetime

from testapp import db
from testapp.common.db import TimestampMixin
    

class User(TimestampMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    slug = db.Column(db.String(80), unique=True, nullable=False)
    pseudoname = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    phone_number = db.Column(db.String(120), unique=True, nullable=True)
    samithi_id = db.Column(db.Integer, db.ForeignKey('samithi.id'), nullable=True)
    samithi = db.relationship('Samithi', backref=db.backref('user', lazy=True))
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_types.id'), nullable=False)
    user_type = db.relationship('Usertype', backref=db.backref('user', lazy=True))

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
