""" IMPORTS """
# import json
from flask import render_template, request, Blueprint, url_for, flash, redirect, session
import requests
from bookworm import os, db
from bookworm.models import Users, Bookshelves

api_key = os.environ.get("GOOGLE_BOOKS_API")

books = Blueprint('books', __name__)


@books.route("/search", methods=["GET", "POST"])
def search():
    """
    SEARCH FUNCTION
    """
    if request.method == "POST":
        payload = {}
        payload["q"] = request.form.get("searchquery")
        payload["key"] = os.environ.get("GOOGLE_BOOKS_API")

        book_request = requests.get("https://www.googleapis.com/books/v1/volumes?fields=items.volumeInfo(title,authors,description,imageLinks/thumbnail)", params=payload)
        results = book_request.json()
        print(results)

        return render_template("search.html", results=results['items'])

    return render_template("search.html")


@books.route("/bookshelves")
def bookshelves():
    """
    BOOKSHELVES FUNCTION
    """
    return render_template("bookshelves.html")


@books.route("/add_bookshelf", methods=["GET", "POST"])
def add_bookshelf():
    """ 
    ADD BOOKSHELF FUNCTION
    """
    if request.method == "POST":
        # gather info from the form to enter into db
        newshelf = Bookshelves(shelf_name=request.form.get("new_shelf"))
        # Add to db
        db.session.add(newshelf)
        db.session.commit()

        # # flash success message & redirect to the bookshelf page
        flash('Bookshelf Created!')
        return redirect(url_for('books.bookshelves'))

    return render_template("add_bookshelf.html")
