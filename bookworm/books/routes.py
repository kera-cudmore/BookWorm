""" IMPORTS """
from flask import render_template, request, Blueprint, url_for, flash, redirect, session
from bson.objectid import ObjectId
import requests
from bookworm import os, db, mongo
from bookworm.models import Bookshelves

api_key = os.environ.get("GOOGLE_BOOKS_API")

books = Blueprint('books', __name__)


@books.route("/search", methods=["GET", "POST"])
def search():
    """
    SEARCH FUNCTION
    Creates an API request to google books API using form input
    Saves request to variable that is passed back to the template
    If error returning request flash message & redirect to search
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
            
            return render_template("search.html", results=results['items'])
        except:
            flash('There was an error. Please try another search term')
            return redirect(url_for("books.search"))
    return render_template("search.html")


@books.route("/bookshelves")
def bookshelves():
    """
    BOOKSHELVES FUNCTION
    Returns all bookshelves from the db in alphabetical order to a variable
    and passes to the template
    """
    bookshelves = list(
        Bookshelves.query.order_by(
            Bookshelves.shelf_name).all())
    return render_template("bookshelves.html", bookshelves=bookshelves)


@books.route("/add_bookshelf", methods=["GET", "POST"])
def add_bookshelf():
    """
    ADD BOOKSHELF FUNCTION
    Creates a new entry in bookshelves table with data from form
    flash message confirming successful creation & redirects to bookshelf page
    """
    # Defensive programming - prevents users creating bookshelf unless signed
    # in
    if "user" not in session:
        flash("You need to be logged in to create a bookshelf")
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        newshelf = Bookshelves(
            shelf_name=request.form.get("new_shelf"),
            created_by=session["user"])

        db.session.add(newshelf)
        db.session.commit()
        flash('New Bookshelf Created!')
        return redirect(url_for('books.bookshelves'))
    return render_template("add_bookshelf.html")


@books.route("/edit_bookshelf/<int:bookshelf_id>", methods=["GET", "POST"])
def edit_bookshelf(bookshelf_id):
    """
    EDIT BOOKSHELF FUNCTION
    Gets bookshelf id or gives 404 error if there isn't one
    Takes form data and updates the db then redirects to bookshelves page
    """

    # Defensive Programming - only the user who created a bookshelf can edit
    # if logged in
    bookshelf = Bookshelves.query.get_or_404(bookshelf_id)

    if "user" not in session or session["user"] != bookshelf.created_by:
        flash("You can only edit your own bookshelves")
        return redirect(url_for("books.bookshelves"))


    if request.method == "POST":
        bookshelf.shelf_name = request.form.get("edit_shelf")
        db.session.commit()
        flash("Your Bookshelf has been edited successfully")
        return redirect(url_for("books.bookshelves"))

    return render_template("edit_bookshelf.html", bookshelf=bookshelf)


@books.route("/delete_bookshelf/<int:bookshelf_id>")
def delete_bookshelf(bookshelf_id):
    """ DELETE BOOKSHELF FUNCTION
    Gets bookshelf id or gives 404 error if there isn't one
    Deletes the bookshelf & commits to the db
    Deletes all books that have that bookshelf ID (cascade deletion)
    Flash message to confirm deletion & redirects the user to
    the bookshelves page
    """

    # Defensive Programming - only user who created bookshelf can delete if
    # logged in
    bookshelf = Bookshelves.query.get_or_404(bookshelf_id)

    if "user" not in session or session["user"] != bookshelf.created_by:
        flash("You can only delete your own bookshelves")
        return redirect(url_for("books.bookshelves"))

    db.session.delete(bookshelf)
    db.session.commit()
    mongo.db.books.delete_many({"bookshelf_id": str(bookshelf_id)})
    flash("Bookshelf Deleted")
    return redirect(url_for("books.bookshelves"))


@books.route("/populate_review", methods=["GET", "POST"])
def populate_review():
    """
    POPULATE REVIEW FUNCTION
    Takes gbook_id from chosen book and runs request to API for that books data
    API request saved as a dictionary which is then passed to the the
    add review function to allow fields to be prepopulated
    """
    bookshelves = list(
        Bookshelves.query.order_by(
            Bookshelves.shelf_name).all())

    gbook_id = request.args.get('gbook_id')
    book = {}
    book["q"] = (gbook_id)
    book["key"] = os.environ.get("GOOGLE_BOOKS_API")
    # API Request
    book_request = requests.get(
        "https://www.googleapis.com/books/v1/volumes",
        params=book)
    # Results returned from the request
    review_book = book_request.json()

    # Dictionary containing information needed to prepopulate add review form
    shelve_book = {
        "title": review_book['items'][0]['volumeInfo']['title'],
        "authors": review_book['items'][0]['volumeInfo']['authors'],
        "thumbnail": review_book['items'][0]['volumeInfo']['imageLinks']['thumbnail']}

    return render_template(
        "add_review.html",
        shelve_book=shelve_book,
        bookshelves=bookshelves)


@books.route("/add_review", methods=["GET", "POST"])
def add_review():
    """
    ADD REVIEW FUNCTION
    queries the bookshelves db and passes results to the template
    Inserts a new document in books collection with data from form
    flash message confirming success & redirects to books page
    """
    # Defensive programming - prevents users creating review unless signed in
    if "user" not in session:
        flash("You need to be logged in to add a review")
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        book_review = {
            "title": request.form.get("book_title"),
            "author": request.form.get("book_author"),
            "cover": request.form.get("cover_url"),
            "rating": request.form.get("rating"),
            "review": request.form.get("book_review"),
            "notes": request.form.get("book_notes"),
            "created_by": session["user"],
            "bookshelf_id": request.form.get("bookshelf_id")
        }

        mongo.db.books.insert_one(book_review)
        flash("Book Successfully Shelved")
        return redirect(url_for("books.view_books"))

    bookshelves = list(
        Bookshelves.query.order_by(
            Bookshelves.shelf_name).all())
    return render_template("add_review.html", bookshelves=bookshelves)


@books.route("/edit_review/<books_id>", methods=["GET", "POST"])
def edit_review(books_id):
    """
    EDIT REVIEW FUNCTION
    Queries the bookshelves db and passes results to the template
    Finds document with the books_id in the collection & passes to template
    Updates the document with the form data
    Flash success message and redirects to books page
    """

    # Defensive programming - allows only the user who created review to edit
    # if they are logged in
    book_review = mongo.db.books.find_one({"_id": ObjectId(books_id)})

    if "user" not in session or session["user"] != book_review["created_by"]:
        flash("You can only edit your own book reviews")
        return redirect(url_for("books.view_books"))

    if request.method == "POST":
        submit = {
            "title": request.form.get("book_title"),
            "author": request.form.get("book_author"),
            "cover": request.form.get("cover_url"),
            "rating": request.form.get("rating"),
            "review": request.form.get("book_review"),
            "notes": request.form.get("book_notes"),
            "created_by": session["user"],
            "bookshelf_id": request.form.get("bookshelf_id")
        }

        mongo.db.books.update_one(
            {"_id": ObjectId(books_id)}, {"$set": submit})
        flash("Review Successfully Updated")
        return redirect(url_for("books.view_books"))

    bookshelves = list(
        Bookshelves.query.order_by(
            Bookshelves.shelf_name).all())
    return render_template(
        "edit_review.html",
        book_review=book_review,
        bookshelves=bookshelves)


@books.route("/view_books")
def view_books():
    """
    VIEW BOOKS FUNCTION
    queries the books collection & passes the results to the template
    """
    display_books = list(mongo.db.books.find())
    return render_template("books.html", display_books=display_books)


@books.route("/delete_book/<books_id>")
def delete_book(books_id):
    """
    DELETE BOOK FUNCTION
    Uses the books_id from the chosen book to query the books collection
    Deletes the document from the collection
    Flash success message & redirects to books page
    """
    mongo.db.books.delete_one({"_id": ObjectId(books_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("books.view_books"))
