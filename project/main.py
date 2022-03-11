# This file contains the routes for the non-auth portions of the app


# Import necessary modules
from flask import Blueprint, render_template
from . import db

# Initialize main
main = Blueprint('main', __name__)

# index route
@main.route('/')
def index():
    return render_template('index.html')
# route for profile
@main.route('/profile')
def profile():
    return render_template('profile.html')
