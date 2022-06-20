"""
IMPORTS
db from bookworm - to define the database structure
"""

from bookworm import db


class Users(db.Model):
    # Schema for the Users model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(260), unique=True, nullable=False) 
    # password string is 260 chars so hashed password can be stored in db

    def __repr__(self):
            # __repr__ to represent itself in the form of a string
            return self.username





class Bookshelves(db.Model):
    # Schema for the Bookshelves model
    id = db.Column(db.Integer, primary_key=True)
    shelf_name = db.Column(db.String(25), unique=True, nullable=False)
    
    
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.shelf_name