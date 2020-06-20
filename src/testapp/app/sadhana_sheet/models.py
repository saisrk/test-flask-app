from testapp import db


class SadhanaSheet(db.Model):
    __tablename__ = 'sadhana_sheet'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    slug = db.Column(db.String(80), unique=True, nullable=False)
    month = db.Column(db.String(80), nullable=False)
    year = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<SadhanaSheet %r>' % self.name


class UserSadhana(db.Model):
    __tablename__ = 'user_sadhana'

    id = db.Column(db.Integer, primary_key=True)
    sadhana_sheet_id = db.Column(db.Integer, db.ForeignKey('sadhana_sheet.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    do_wakeup = db.Column(db.Boolean, default=False)
    do_prayer = db.Column(db.Boolean, default=False)
    do_exercise = db.Column(db.Boolean, default=False)
    do_listen = db.Column(db.Boolean, default=False)
    do_namasmarana = db.Column(db.Boolean, default=False)
    do_drink_water = db.Column(db.Boolean, default=False)
    do_no_tv = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<UserSadhana %r>' % self.id