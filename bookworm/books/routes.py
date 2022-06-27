""" IMPORTS """
from flask import render_template, request, Blueprint, url_for, flash, redirect, session
from bookworm import db
from bookworm.models import Users, Bookshelves

books = Blueprint('books', __name__)


@books.route("/search")
def search():
    """
    SEARCH FUNCTION
    """
    return render_template("search.html")
