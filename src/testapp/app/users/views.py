from flask import Blueprint, jsonify, render_template, flash, request
from flask_login import login_user, login_url

from .services import get_all_users

users_blueprint = Blueprint('users', __name__, template_folder='../templates')


@users_blueprint.route('/users')
def index():
    # return get_all_users()
    return render_template('users.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         login_user(user)
#         flash('Logged in successfully.')
#         next = request.args.get('next')
#         if not is_safe_url(next):
#             return flask.abort(400)
#         return flask.redirect(next or flask.url_for('index'))
#     return flask.render_template('login.html', form=form)
