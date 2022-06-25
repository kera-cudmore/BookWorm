"""
IMPORT os, Flask & SQLAlchemy
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# IMPORT env if there is an env.py file
# Used in local dev as not pushed to github & heroku
if os.path.exists("env.py"):
    import env # noqa


app = Flask(__name__)



app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

# noqa - app & db need to be defined first before the routes
from bookworm.users.routes import users
from bookworm.books.routes import books
from bookworm.main.routes import main

app.register_blueprint(users)
app.register_blueprint(books)
app.register_blueprint(main)
