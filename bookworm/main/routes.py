""" IMPORTS """
from flask import render_template, Blueprint

main = Blueprint('main', __name__)


@main.route("/")
def home():
    """
    HOME FUNCTION
    Renders template for the home page
    """
    return render_template("index.html")
