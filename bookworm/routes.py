"""
IMPORTS
flask - render template,
bookworm - app, db,
"""
from flask import render_template
from bookworm import app, db
# from bookworm.models import


@app.route("/")
def home():
    """
    home function will return the rendered template for index.html
    """
    return render_template("index.html")


@app.route("/login")
def login():
    """
    login function will return the rendered template for login.html
    """
    return render_template("login.html")


@app.route("/register")
def register():
    """
    register function will return the rendered template for register.html
    """
    return render_template("register.html")
