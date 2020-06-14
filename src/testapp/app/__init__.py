from flask import jsonify, Blueprint, render_template

ping_blueprint = Blueprint('ping', __name__, template_folder='templates')

@ping_blueprint.route('/ping')
def ping():
    return jsonify(
        {
            'message': 'Pong!'
        }
    )

@ping_blueprint.route('/')
def index():
    return render_template('index.html')
