from flask import jsonify
from flask_jwt_extended import create_access_token

from extensions.jwt import blacklisted_tokens
from models.user import User
from repositories.user_repository import UserRepository


class UserService:

    @staticmethod
    def register(data):
        user = User(name=data["name"], email=data["email"], password=data["password"])
        if not UserRepository.find_by_email(user.email):
            saved_user = UserRepository.save(user)
            return jsonify({"message": "User created", "user": saved_user}), 201
        return {"message": "Email already registered"}, 400

    @staticmethod
    def login(data):
        user = UserRepository.find_by_email(data["email"])
        if not user:
            return jsonify({"message": "Invalid credentials (user not found)"}), 401
        if not user.verify_password(data["password"]):
            return jsonify({"message": "Invalid credentials (password mismatch)"}), 401
        access_token = create_access_token(identity=user.get_id())
        return jsonify({"access_token": access_token}), 200

    @staticmethod
    def logout(jti):
        blacklisted_tokens.add(jti)
        return jsonify({"message": "Successfully logged out"}), 200

    @staticmethod
    def update_profile(user_id, data):
        user = UserRepository.find_by_id(user_id)
        if not user:
            return jsonify({"message": "User not found"}), 404
        update_fields = {}
        if "name" in data:
            update_fields["name"] = data["name"]
        if "email" in data:
            # Check if new email is not already taken
            if UserRepository.find_by_email(data["email"]):
                return jsonify({"message": "Email already registered"}), 400
            update_fields["email"] = data["email"]
        if "password" in data:
            update_fields["password"] = User.hash_password(data["password"])
        if not update_fields:
            return jsonify({"message": "No valid fields to update"}), 400
        # Update user in DB
        user.update(update_fields)
        # Save changes
        mongo = __import__('extensions.database', fromlist=['mongo_tasks']).mongo_tasks
        mongo.db.users.update_one({"_id": user_id}, {"$set": update_fields})
        return jsonify({"message": "Profile updated", "user": update_fields}), 200

    @staticmethod
    def reset_password(email, new_password):
        user = UserRepository.find_by_email(email)
        if not user:
            return jsonify({"message": "User not found"}), 404
        hashed_pw = User.hash_password(new_password)
        mongo = __import__('extensions.database', fromlist=['mongo_tasks']).mongo_tasks
        mongo.db.users.update_one({"_id": user.get_id()}, {"$set": {"password": hashed_pw}})
        return jsonify({"message": "Password reset successful"}), 200

    @staticmethod
    def get_profile(user_id):
        user = UserRepository.find_by_id(user_id)
        if not user:
            return jsonify({"message": "User not found"}), 404
        # Remove password from response
        user.pop("password", None)
        return jsonify({"user": user}), 200

