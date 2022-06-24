""" IMPORTS """
from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from bookworm import app, db
from bookworm.models import Users, Bookshelves


@app.route("/")
def home():
    """
    HOME FUNCTION
    """
    return render_template("index.html")


@app.route("/login")
def login():
    """
LOGIN FUNCTION
    """
    if "user" in session:
        flash("You're already logged in!")
        return redirect(url_for('profile', username=session["user"]))

    if request.method == "POST":
        existing_user = Users.query.filter(
            Users.username == request.form.get("username")).lower()

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))

            else:
                # invalid password match - By using and/or incorrect
                # makes harder to brute force an account
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist - By using and/or incorrect
            # makes harder to brute force an account
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/register")
def register():
    """
    REGISTER FUNCTION
    """
    if request.method == "POST":
        # Check to see if username already exists
        existing_user = Users.query.filter(
            Users.username == request.form.get("username")).lower()

        # If username exists - flash message & reload register page
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # If username doesn't exist in the db
        # gather info from the form to enter into db
        user = Users(
            username=request.form.get("username").lower(),
            email=request.form.get("email").lower(),
            password=generate_password_hash(request.form.get("password")),
        )
        # Add to db
        db.session.add(user)
        db.session.commit()

        # add the user to the session and redirect to the login page
        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")
        return redirect(url_for('login'))

    # renders the register page
    return render_template("register.html")
