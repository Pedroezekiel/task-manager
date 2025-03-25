from flask import jsonify
from flask_jwt_extended import create_access_token
from sqlalchemy.testing.suite.test_reflection import users

from models.user import User
from repositories.user_repository import UserRepository


class UserService:

    @staticmethod
    def register(data):
        user = User(name=data["name"], email=data["email"], password=data["password"])
        saved_user = UserRepository.register(user)
        return jsonify({"message":"User created","user": saved_user}), 201

    @staticmethod
    def login(data):
        user = UserRepository.find_by_email(data["email"])
        if not user or not user.check_password(data["password"]):
            return jsonify({"message":"Invalid credentials"}), 401
        access_token = create_access_token(identity=str(user["_id"]))
        return jsonify({"access_token": access_token}), 200