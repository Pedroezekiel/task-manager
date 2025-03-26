from flask import request
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity

from service.task_service import TaskService

class TaskController:
    @staticmethod
    @jwt_required()
    def create_task():
        user_id = get_jwt_identity()
        data = request.get_json()
        return TaskService.create_task(data, user_id)

    @staticmethod
    @jwt_required()
    def get_task(task_id):
        user_id = get_jwt_identity()
        return TaskService.get_task(task_id, user_id)

    @staticmethod
    @jwt_required()
    def update_task(task_id):
        user_id = get_jwt_identity()
        data = request.get_json()
        return TaskService.update_task(task_id, data, user_id)

    @staticmethod
    @jwt_required()
    def get_all_tasks():
        user_id = get_jwt_identity()
        return TaskService.get_all_tasks(user_id)

    @staticmethod
    @jwt_required()
    def delete_task(task_id):
        user_id = get_jwt_identity()
        return TaskService.delete_task(task_id, user_id)

    @staticmethod
    @jwt_required()
    def change_task_status(task_id, status):
        user_id = get_jwt_identity()
        return TaskService.update_task_status(task_id, status, user_id)



