from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
import os

db = SQLAlchemy()
cors = CORS()
migrate = Migrate()
login_manager = LoginManager()
admin = Admin(name='Bhajan Vikas', template_mode='bootstrap3')


def create_app():
    """
    Application factory for Flask. This factory function will
    take care of initialising the Application and its
    necessary plugins like database, flask apps etc
    which supports the application.
    :return: app => application instance
    """
    # Create the flask application in application factory
    app = Flask(__name__)

    # Use the configuration accordingly
    # TODO: Now only added Development config. Need to dynamically
    #   pick up based on env config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # import the models here
    from testapp.app.users import models
    from testapp.app.attendance import models
    from testapp.app.sadhana_sheet import models

    # Initialising flask plugins including database
    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    admin.init_app(app)

    # Initialise the blueprints by registering them
    # to the application.
    from testapp.app import ping_blueprint
    from testapp.app.users.views import users_blueprint
    from testapp.app.attendance.views import attendance_blueprint
    from testapp.app.dashboard.views import dashboard_blueprint

    from testapp.app.users.admin import users_admin

    app.register_blueprint(ping_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(attendance_blueprint)
    app.register_blueprint(dashboard_blueprint)

    app.register_blueprint(users_admin)

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    from testapp.app.users.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    return app
