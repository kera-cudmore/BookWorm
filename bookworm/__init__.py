""" IMPORTS """
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# IMPORT env if there is an env.py file
# Used in local dev as not pushed to github & heroku
if os.path.exists("env.py"):
    import env # noqa


app = Flask(__name__)


app.config["SECRET_KEY"]=os.environ.get("SECRET_KEY")


# if development == True it will use the local db
# if false it will use the db on heroku
# if the heroku db has postgres:// it will update it with the correct value
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://",  "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri


db = SQLAlchemy(app)


# noqa - app & db need to be defined first before the routes
from bookworm.auth.routes import auth
from bookworm.books.routes import books
from bookworm.main.routes import main
app.register_blueprint(auth)
app.register_blueprint(books)
app.register_blueprint(main)
