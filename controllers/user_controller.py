from flask import request
from flask_jwt_extended import jwt_required, get_jwt

from service.user_service import UserService


class UserController:

    @staticmethod
    def register_user():
        data = request.get_json()
        if not data["name"] or not data["password"] or not data["email"]:
            return {"message": "Missing required parameters"}, 400
        return UserService.register(data)

    @staticmethod
    def user_login():
        data = request.get_json()
        if not data["password"] or not data["email"]:
            return {"message": "Missing required parameters"}, 400
        return UserService.login(data)

    @staticmethod
    @jwt_required()
    def user_logout():
        print("-------------------------")
        jti = get_jwt()["jti"]
        return UserService.logout(jti)

