# This file contains the preliminary authentication routes defined for the app

# Import the necessary modules
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

# Initialize auth
auth = Blueprint('auth', __name__)

#creating the routes for the different portions of the page

# Login route
@auth.route('/login')
def login():
    return render_template('login.html')

# signup route
@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():

    # validate and add user to database
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # Tackle reduandancy with account creation
    user = User.query.filter_by(email=email).first() # checks if a user already exists, if user is returned, the the email is already contained in the database. 

    if user: # if user already exists, redirect back to signup page.

        #Alerts the user that the email already exists
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Also, Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add new user to the database
    db.session.add(new_user)
    db.session.commit()



    # validate and add user to database goes here
    return redirect(url_for('auth.login'))
# Logout for the route
@auth.route('/logout')
def logout():
    return render_template('signup.html')
