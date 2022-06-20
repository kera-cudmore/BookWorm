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

from bookworm import routes # noqa - app & db need to be defined first
