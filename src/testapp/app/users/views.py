from flask import Blueprint, jsonify, render_template

from .services import get_all_users

users_blueprint = Blueprint('users', __name__, template_folder='../templates')


@users_blueprint.route('/users')
def index():
    # return get_all_users()
    return render_template('users.html')


@users_blueprint.route('/users/<id>', methods=['GET'])
def get(id):
    pass


@users_blueprint.route('/users', methods=['POST'])
def add():
    pass
