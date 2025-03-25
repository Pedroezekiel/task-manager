from flask import Blueprint
from controllers.user_controller import UserController


class UserRoutes(Blueprint):
    def __init__(self):
        super().__init__("user_routes", __name__, url_prefix="/api/users")
        self.register_routes()

    def register_routes(self):
        self.add_url_rule("/", view_func=UserController.register_user, methods=["POST"])
        self.add_url_rule("/", view_func=UserController.user_login, methods=["GET"])

user_routes = UserRoutes()