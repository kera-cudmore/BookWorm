""" IMPORTS """
import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
# IMPORT env if there is an env.py file
# Used in local dev as not pushed to github & heroku
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

# if development == True it will use the local db
# if false it will use the db on heroku
# if the heroku db has postgres:// it will update it with the correct value
if os.environ.get("DEVELOPMENT") == "True":
    # local db
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://",  "postgresql://", 1)
    # heroku db
    app.config["SQLALCHEMY_DATABASE_URI"] = uri


db = SQLAlchemy(app)
migrate = Migrate(app, db)
mongo = PyMongo(app)


# app & db need to be defined first before the routes
from bookworm.auth.routes import auth  # noqa: E402
from bookworm.books.routes import books  # noqa: E402
from bookworm.main.routes import main  # noqa: E402
from bookworm.error_handlers.routes import error  # noqa: E402
app.register_blueprint(auth)  # noqa: E402
app.register_blueprint(books)  # noqa: E402
app.register_blueprint(main)  # noqa: E402
app.register_blueprint(error)  # noqa: E402
