from flask import render_template, Blueprint

dashboard_blueprint = Blueprint('dashboard', __name__, template_folder='../templates')


@dashboard_blueprint.route('/dashboard')
def index():
    return render_template('dashboard.html')