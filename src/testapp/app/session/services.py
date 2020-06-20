from datetime import datetime
from werkzeug.exceptions import BadRequest

from .models import Session, Attendance
from testapp.app.users.models import User

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