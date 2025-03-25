from flask import request

from service.task_service import TaskService

class TaskController:
    @staticmethod
    def create_task():
        data = request.get_json()
        return TaskService.create_task(data)

    @staticmethod
    def get_task(task_id):
        return TaskService.get_task(task_id)

    @staticmethod
    def update_task(task_id):
        data = request.get_json()
        return TaskService.update_task(task_id, data)

    @staticmethod
    def get_all_tasks():
        return TaskService.get_all_tasks()



