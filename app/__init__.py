from flask import Flask

# SQl toolkit for python
from flask_sqlalchemy import SQLAlchemy

# for styling css
from flask_bootstrap import Bootstrap

# import config options form config
from config import config_options

# importing used for login
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()

db = SQLAlchemy()


def create_app(config_name):

    # intiating flask us a app
    app = Flask(__name__)

    # getting bootstrap form app
    bootstrap.init_app(app)

    # Initializing flask extensions
    db.init_app(app)

    # allows to get settings form config
    app.config.from_object(config_options[config_name])
    # intializing login manager
    login_manager.init_app(app)

    # intiate flask login
    login_manager.init_app(app)

    # Registering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint of the authnication
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    return app
