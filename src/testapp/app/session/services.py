from datetime import datetime
from werkzeug.exceptions import BadRequest

from .models import Session, Attendance
from testapp.app.users.models import User
from testapp import db

def get_all_sessions():
    sessions = Session.query.all()
    upcoming_session = [session for session in sessions if session.old_session][0]
    previous_sessions = [session for session in sessions if not session.old_session]
    return upcoming_session, previous_sessions


def get_attendance_for_session(session_id):
    session = Session.query.get(session_id)
    if not session:
        return BadRequest('No session found')

    attendance_data = Attendance.query.filter_by(session_id=session.id)
    return attendance_data, session

def edit_attendance_for_session(session_id):
    session = Session.query.get(session_id)
    user_data = User.query.filter_by()
    user_data = [user for user in user_data]
    return session, user_data

def add_attendance_for_user(session_id, user_id, status):
    session = Session.query.get(session_id)
    user = User.query.get(user_id)

    attendance = Attendance.query.filter_by(session_id=session_id, user_id=user_id)
    if attendance:
        attendance.status = status
        db.session.add(attendance)
        db.session.commit()
    else:
        new = Attendance(
            session_id=session_id,
            user_id=user_id,
            status=status
        )
        db.session.add(new)
        db.session.commit()

    return True
