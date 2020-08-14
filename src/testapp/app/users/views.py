from flask import Blueprint, render_template, jsonify, request

from .services import get_all_users, get_user_by_email, get_user_by_id, add_user, update_user

users_blueprint = Blueprint('users', __name__, template_folder='../templates')


@users_blueprint.route('/users')
def index():
    users = get_all_users()
    return jsonify(users)


@users_blueprint.route('/users/<id>')
def get_user(id):
    user = get_user_by_id(id)
    if user:
        return jsonify(user)
    else:
        return {
            "message": "No user found for id %s" % id
        }

@users_blueprint.route('/users', methods=['POST'])
def user_addition():
    request_body = request.get_json()
    users = add_user(request_body)
    return jsonify(users)


@users_blueprint.route('/users/<id>', methods=['PUT'])
def user_updation(id):
    request_body = request.get_json()
    users = update_user(id, request_body)
    return jsonify(users)