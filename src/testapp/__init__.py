from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
import os

db = SQLAlchemy()
cors = CORS()
migrate = Migrate()


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

    # Initialising flask plugins including database
    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)

    # Initialise the blueprints by registering them
    # to the application.
    from testapp.app import ping_blueprint
    from testapp.app.users.views import users_blueprint

    app.register_blueprint(ping_blueprint)
    app.register_blueprint(users_blueprint)

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
