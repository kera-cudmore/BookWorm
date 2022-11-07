""" IMPORTS """
from flask import (render_template, request, Blueprint, url_for, redirect,
                   flash, session)
from werkzeug.security import generate_password_hash, check_password_hash
from bookworm import db
from bookworm.models import Users

auth = Blueprint('auth', __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    """
    REGISTER FUNCTION
    Checks if username exists:
    Existing - flash message & redirect to register page
    New - use form data to add to db, flash message & redirect to login
    """
    if request.method == "POST":
        # Check to see if username already exists
        existing_user = Users.query.filter(
            Users.username == request.form.get("username").lower()).all()

        # If username exists - flash message & reload register page
        if existing_user:
            flash("This username already exists, please try another username.")
            return redirect(url_for("auth.register"))

        # If username doesn't exist in the db gather info from the form to
        # enter into db
        newuser = Users(
            username=request.form.get("username").lower(),
            email=request.form.get("email").lower(),
            password=generate_password_hash(request.form.get("password")),
        )
        # Add to db
        db.session.add(newuser)
        db.session.commit()

        # Add the user to the session and redirect to the login page
        flash('Registration successful!')
        return redirect(url_for('auth.login'))

    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    """
    LOGIN FUNCTION
    Checks to see if the user exists in the db and saves to variable
    If there is a record, checks the hashed password against
    the form input password
    If they match, flash message and redirect to profile page
    If password doesn't match or no user in db flash message
    and redirect to login
    """
    if request.method == "POST":
        existing_user = Users.query.filter(
            Users.username == request.form.get("username").lower()).all()

        if existing_user:
            if check_password_hash(
                    existing_user[0].password,
                    request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome back, {}".format(
                    request.form.get("username").capitalize()))
                return redirect(
                    url_for(
                        "auth.profile",
                        username=session["user"]))

            else:
                # invalid password match - By using and/or incorrect makes
                # harder to brute force an account
                flash("Incorrect Username and/or Password")
                return redirect(url_for("auth.login"))

        else:
            # username doesn't exist - By using and/or incorrect
            # makes harder to brute force an account
            flash("Incorrect Username and/or Password")

    return render_template("login.html")


@auth.route("/profile")
def profile():
    """
    PROFILE FUNCTION
    """
    return render_template("profile.html")


@auth.route("/logout")
def logout():
    """
    LOGOUT FUNCTION
    Removes the user from the session, flash message & redirect to home page
    """
    session.pop("user")
    flash("You have been logged out.")
    return render_template("index.html")
