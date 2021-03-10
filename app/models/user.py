from . import db
from .abc import BaseModel, MetaBaseModel
from dataclasses import dataclass

"""
@dataclass makes the class return a json string
"""


@dataclass
class User(db.Model):
    """The user model"""
    id: int
    username: str
    email: str

    # __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
