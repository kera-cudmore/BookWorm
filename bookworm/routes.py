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
    Home function will return the rendered template for base.html
    """
    return render_template("base.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")
