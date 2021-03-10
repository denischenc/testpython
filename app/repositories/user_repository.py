
from . import db
from app.models import User
from flask import jsonify


class UserRepository:
    def __init__(self):
        super().__init__()

    def get_all_users(self):
        users = User.query.all()
        return users

    def get_user_by_id(self):
        pass

    def search_user(self):
        pass

    def add_user(self):
        pass

    def delete_user(self):
        pass

    def update_user(self):
        pass
