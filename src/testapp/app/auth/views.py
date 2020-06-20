from flask import Blueprint, jsonify, render_template, flash, request, abort, redirect, url_for
from flask_login import login_user, login_required,logout_user

from testapp.app.users.services import get_all_users, get_user_by_email
from .forms import LoginForm

auth_blueprint = Blueprint('auth', __name__, template_folder='../templates')


@auth_blueprint.route('/auth/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.data.get('email')
        password = form.data.get('password')
        user = get_user_by_email(email)
        if user:
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('users.index'))
        else:
            flash('No user found.')
    return render_template('login.html', form=form)


@auth_blueprint.route('/auth/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('ping.index'))