""" IMPORTS """
from flask import render_template, request, Blueprint, url_for, flash, redirect, session
from bson.objectid import ObjectId
import requests
from bookworm import os, db, mongo
from bookworm.models import Users, Bookshelves

api_key = os.environ.get("GOOGLE_BOOKS_API")

books = Blueprint('books', __name__)


@books.route("/search", methods=["GET", "POST"])
def search():
    """
    SEARCH FUNCTION
    """
    if request.method == "POST":
        try:
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
        except:
           flash('There was an error. Please try another search term')
           return redirect (url_for("books.search"))
           
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
    if "user" not in session:
        flash("You need to be logged in to create a bookshelf")
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        # gather info from the form to enter into db
        newshelf = Bookshelves(shelf_name=request.form.get("new_shelf"), created_by=session["user"]
                               )
        # Add to db
        db.session.add(newshelf)
        db.session.commit()
        # flash success message & redirect to the bookshelf page
        flash('New Bookshelf Created!')
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




@books.route("/populate_review", methods=["GET", "POST"])
def populate_review():
    """
    POPULATE REVIEW FUNCTION
    this function should take the id from the book button on search page, run an api request for that id
    and pass that variable onto the add_review page so the book title, author & cover can be pre-populated
    """
    bookshelves = list(Bookshelves.query.order_by(Bookshelves.shelf_name).all())

    gbook_id = request.args.get('gbook_id')
    book = {}
    book["q"] = (gbook_id)
    book["key"] = os.environ.get("GOOGLE_BOOKS_API")
    # API Request
    book_request = requests.get("https://www.googleapis.com/books/v1/volumes", params=book)
    # Results returned from the request
    review_book = book_request.json()
    
    # Create new dictionary for book with only the information needed to be displayed in the review section
    shelve_book = {
        "title": review_book['items'][0]['volumeInfo']['title'],
        "authors": review_book['items'][0]['volumeInfo']['authors'],
        "thumbnail": review_book['items'][0]['volumeInfo']['imageLinks']['thumbnail']
    }

    return render_template("add_review.html", shelve_book=shelve_book, bookshelves=bookshelves)


@books.route("/add_review", methods=["GET", "POST"])
def add_review():
    """
    ADD REVIEW FUNCTION
    takes the information from the input fields and saves them to mongodb
    """
    if "user" not in session:
        flash("You need to be logged in to add a review")
        return redirect(url_for("auth.login"))

    bookshelves = list(Bookshelves.query.order_by(Bookshelves.shelf_name).all())
    if request.method == "POST":
        book_review = {
            "title": request.form.get("book_title"),
            "author": request.form.get("book_author"),
            "cover": request.form.get("cover_url"),
            "rating": request.form.get("rating"),
            "review": request.form.get("book_review"),
            "notes": request.form.get("book_notes"),
            "created_by": session["user"],
            "shelf_name": request.form.get("bookshelf_id")
        }

        mongo.db.books.insert_one(book_review)
        flash("Book Successfully Shelved")
        return redirect(url_for("books.view_books"))
       
    return render_template("add_review.html", bookshelves=bookshelves)


@books.route("/edit_review/<books_id>", methods=["GET", "POST"])
def edit_review(books_id):
    """
    EDIT REVIEW FUNCTION
    """
    if request.method == "POST":
        submit = {
            "title": request.form.get("book_title"),
            "author": request.form.get("book_author"),
            "cover": request.form.get("cover_url"),
            "rating": request.form.get("rating"),
            "review": request.form.get("book_review"),
            "notes": request.form.get("book_notes"),
            "created_by": session["user"],
            "shelf_name": request.form.get("bookshelf_id")
        }

        mongo.db.books.update_one({"_id": ObjectId(books_id)}, {"$set": submit})
        flash("Review Successfully Updated")
        return redirect(url_for("books.view_books"))

    book_review = mongo.db.books.find_one({"_id": ObjectId(books_id)})
    bookshelves = list(Bookshelves.query.order_by(Bookshelves.shelf_name).all()) 
    return render_template("edit_review.html", book_review=book_review, bookshelves=bookshelves)


@books.route("/view_books")
def view_books():
    """
    VIEW BOOKS FUNCTION
    """
    display_books = list(mongo.db.books.find())
    return render_template("books.html", display_books=display_books)


@books.route("/delete_book/<books_id>")
def delete_book(books_id):
    """
    DELETE BOOK FUNCTION
    """
    mongo.db.books.delete_one({"_id": ObjectId(books_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("books.view_books"))