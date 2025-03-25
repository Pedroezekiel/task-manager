from flask import jsonify
from flask_jwt_extended import create_access_token

from extensions.auth import blacklisted_tokens
from models.user import User
from repositories.user_repository import UserRepository


class UserService:

    @staticmethod
    def register(data):
        user = User(name=data["name"], email=data["email"], password=data["password"])
        if not UserRepository.find_by_email(user.email):
            print("--------------------------===================")
            saved_user = UserRepository.register(user)
            return jsonify({"message": "User created", "user": saved_user}), 201
        return {"message": "Email already registered"}, 400

    @staticmethod
    def login(data):
        user = UserRepository.find_by_email(data["email"])

        print("User found:", user)
        if not user:
            return jsonify({"message": "Invalid credentials (user not found)"}), 401

        if not user.verify_password(data["password"]):
            return jsonify({"message": "Invalid credentials (password mismatch)"}), 401

        access_token = create_access_token(identity=str(user.get_id()))

        return jsonify({"access_token": access_token}), 200

    @staticmethod
    def logout(jti):
        print("============++++++++++++++++++++++")
        blacklisted_tokens.add(jti)
        return jsonify({"message": "Successfully logged out"}), 200

