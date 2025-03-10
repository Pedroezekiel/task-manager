from flask import Blueprint, request, jsonify
from controllers.task_controller import TaskController

class TaskRoutes(Blueprint):
    def __init__(self):
        super().__init__("task_routes", __name__, url_prefix="/api/tasks")
        self.register_routes()

    def register_routes(self):
        """Registers all task-related routes."""
        self.add_url_rule("/", view_func=TaskController.create_task, methods=["POST"])
        self.add_url_rule("/<task_id>", view_func=TaskController.get_task, methods=["GET"])

task_routes = TaskRoutes()