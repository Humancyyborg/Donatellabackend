# This file is generally for the setup of the flask app to encapsulate the model

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initializing the SQLAlchemy for future use in the models later
db = SQLAlchemy()

# defining the function
def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    # plan for auth routes 
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # plan for non-auth portions of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
