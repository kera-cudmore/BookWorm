from flask import render_template, request, Blueprint, url_for, redirect, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from bookworm.models import Users, Bookshelves

auth = Blueprint('auth', __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    """
    REGISTER FUNCTION
    """
    if request.method == "POST":
        # Check to see if username already exists
        existing_user = Users.query.filter(
            Users.username == request.form.get("username").lower()).all

        # If username exists - flash message & reload register page
        if existing_user:
            flash("This username already exists, please try another username.")
            return redirect(url_for("auth.register"))

        # If username doesn't exist in the db
        # gather info from the form to enter into db
        newuser = Users(
            username=request.form.get("username").lower(),
            email=request.form.get("email").lower(),
            password=generate_password_hash(request.form.get("password")),
        )
        # Add to db
        db.session.add(newuser)
        db.session.commit()

        # # add the user to the session and redirect to the login page
        # session["user"] = request.form.get("username").lower()
        flash('Registration successful!')
        return redirect(url_for('auth./login'))

    # renders the register page
    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    """
LOGIN FUNCTION
    """
    if request.method == "POST":
        existing_user = Users.query.filter(
            Users.username == request.form.get("username")).lower()

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "auth.profile", username=session["user"]))

            else:
                # invalid password match - By using and/or incorrect
                # makes harder to brute force an account
                flash("Incorrect Username and/or Password")
                return redirect(url_for("auth.login"))

        else:
            # username doesn't exist - By using and/or incorrect
            # makes harder to brute force an account
            flash("Incorrect Username and/or Password")

    return render_template("login.html")


@auth.route("/profile")
def profile():
    return render_template("profile.html")
