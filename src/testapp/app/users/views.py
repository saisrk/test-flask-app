from flask import Blueprint, render_template

from .services import get_all_users, get_user_by_email

users_blueprint = Blueprint('users', __name__, template_folder='../templates')


@users_blueprint.route('/users')
def index():
    users = get_all_users()
    return render_template('users.html', users=users)
