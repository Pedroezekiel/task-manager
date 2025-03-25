from flask import Blueprint
from controllers.task_controller import TaskController

class TaskRoutes(Blueprint):
    def __init__(self):
        super().__init__("task_routes", __name__, url_prefix="/api/tasks")
        self.register_routes()

    def register_routes(self):
        """Registers all task-related routes."""
        self.add_url_rule("/", view_func=TaskController.create_task, methods=["POST"])
        self.add_url_rule("/<task_id>", view_func=TaskController.get_task, methods=["GET"])
        self.add_url_rule("/<task_id>", view_func=TaskController.update_task, methods=["PUT"])
        self.add_url_rule("/all", view_func=TaskController.get_all_tasks, methods=["GET"])
        self.add_url_rule("/<task_id>", view_func=TaskController.delete_task, methods=["DELETE"])
        self.add_url_rule("/<task_id>/<status>", view_func=TaskController.complete_task, methods=["PUT"])


task_routes = TaskRoutes()