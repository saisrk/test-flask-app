from flask import render_template, Blueprint
from flask_login import login_required

from .services import get_all_sessions, get_attendance_for_session

session_blueprint = Blueprint('session', __name__, template_folder='../templates')


@session_blueprint.route('/session')
def index():
    upcoming, previous = get_all_sessions()
    return render_template('session.html', upcoming=upcoming, previous=previous)


@session_blueprint.route('/session/<int:id>/attendance')
def get_attendance(id):
    attendance, session = get_attendance_for_session(id)
    return render_template('attendance.html', attendance=attendance, session=session)