""" IMPORTS """
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
        #try:
            payload = {}
            payload["q"] = request.form.get("searchquery")
            payload["key"] = os.environ.get("GOOGLE_BOOKS_API")
            # API Request
            book_request = requests.get("https://www.googleapis.com/books/v1/volumes?&maxResults=30&projection=lite", params=payload)
            # Results returned from the request
            results = book_request.json()
            # Prints results to the terminal
            print(results)
            return render_template("search.html", results=results['items'])
        #except:
        #    flash('There was an error. Please try another search term')
    return render_template("search.html")


@books.route("/bookshelves")
def bookshelves():
    """
    BOOKSHELVES FUNCTION
    """
    bookshelves = list(Bookshelves.query.order_by(Bookshelves.shelf_name).all())
    return render_template("bookshelves.html", bookshelves=bookshelves)


@books.route("/add_bookshelf", methods=["GET", "POST"])
def add_bookshelf():
    """ 
    ADD BOOKSHELF FUNCTION
    """
    if request.method == "POST":
        # gather info from the form to enter into db
        newshelf = Bookshelves(shelf_name=request.form.get("new_shelf"),
                                created_by=session["user"])
        # Add to db
        db.session.add(newshelf)
        db.session.commit()
        # flash success message & redirect to the bookshelf page
        flash('Bookshelf Created!')
        return redirect(url_for('books.bookshelves'))
    return render_template("add_bookshelf.html")


@books.route("/edit_bookshelf/<int:bookshelf_id>", methods=["GET", "POST"])
def edit_bookshelf(bookshelf_id):
    """
    EDIT BOOKSHELF FUNCTION
    retrieves the bookshelf id or throws 404 error if there isn't one
    """
    bookshelf = Bookshelves.query.get_or_404(bookshelf_id)
    if request.method == "POST":
        bookshelf.shelf_name = request.form.get("edit_shelf")
        db.session.commit()
        return redirect(url_for("books.bookshelves"))
    return render_template("edit_bookshelf.html", bookshelf=bookshelf)


@books.route("/delete_bookshelf/<int:bookshelf_id>")
def delete_bookshelf(bookshelf_id):
    """ DELETE BOOKSHELF FUNCTION
    retrieves the bookshelf id or throws 404 error if there isn't one
    deletes the bookshelf & commits to the db
    redirects the user to the bookshelves page
    """
    bookshelf = Bookshelves.query.get_or_404(bookshelf_id)
    db.session.delete(bookshelf)
    db.session.commit()
    return redirect(url_for("books.bookshelves"))


# @books.route("/populate_review", methods=["GET", "POST"])
# def populate_review():
#     """
#     POPULATE REVIEW FUNCTION
#     this function takes the id from the book button & calls the api to populate the add review inputs with title, author & cover
#     """
#     if request.method = POST:
        
#     return render_template("add_review.html")


@books.route("/add_review", methods=["GET", "POST"])
def add_review():
    """
    ADD REVIEW FUNCTION
    """
    bookshelves = list(Bookshelves.query.order_by(Bookshelves.shelf_name).all())
    if request.method == POST:
        review = {
            "title": request.form.get("bookTitle"),
            "author": request.form.get("bookAuthor"),
            "cover": request.form.get(""),
            "rating": request.form.get(""),
            "review": request.form.get("bookReview"),
            "notes": request.form.get("bookNotes"),
            "created_by": session["user"],
            "shelf_name": request.form.get("bookshelf_id")
        }
        mongo.db.books.insert_one(review)
        flash("Book Successfully Shelved")
        return redirect(url_for('books.bookshelves'))

    else:
        payload = {}
        payload["/"] = ("book_id")
        payload["key"] = os.environ.get("GOOGLE_BOOKS_API")
        # API Request
        single_request = requests.get("https://www.googleapis.com/books/v1/volumes", params=payload)
        # Results returned from the request
        review_book = single_request.json()
        # Prints results to the terminal
        print(review_book)

    return render_template("add_review.html", book_id={{ result.id }})
