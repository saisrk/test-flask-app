from flask import render_template, Blueprint

attendance_blueprint = Blueprint('attendance', __name__, template_folder='../templates')


@attendance_blueprint.route('/attendance')
def index():
    return render_template('attendance.html')