""" IMPORTS """
from flask import render_template, request, Blueprint, redirect, flash, url_for, session
from bookworm import db
from bookworm.models import Users, Bookshelves

main = Blueprint('main', __name__)


@main.route("/")
def home():
    """
    HOME FUNCTION
    """
    return render_template("index.html")
