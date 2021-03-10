# exporting or exposing the db object of SQLAlchemy to be intitialised by the flask app/ server object
# and use throughout the application from this package only

# to use the SQLAlchemy object just do
# `from app.database import db`

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
