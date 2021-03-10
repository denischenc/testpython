
from flask import current_app as app, Blueprint, request, jsonify
from app.database import db
from app.models.user import User
from app.repositories import UserRepository


USER_BLUEPRINT = Blueprint('users', __name__)


@USER_BLUEPRINT.route('/')
def index():
    all_users = UserRepository().get_all_users()
    print(all_users)
    return jsonify(success=True, message=all_users)


@USER_BLUEPRINT.route('/adduser', methods=["POST"])
def add_user():
    data = request.json
    print(data)
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    added_user = User.query.all()

    return jsonify(success=True, message={"userId": user.id}), 201
