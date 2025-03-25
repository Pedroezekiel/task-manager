from datetime import datetime

from flask import jsonify

from enums.task_status import TaskStatusEnum
from models.task import Task
from repositories.task_repository import TaskRepository
from serializers.task_serializer import TaskSerializer


class TaskService:

    @staticmethod
    def create_task(data):
        task = Task(title=data["title"],description=data["description"])
        saved_task = TaskRepository.save(task)
        return jsonify({"message":"Task created","task": saved_task}), 201

    @staticmethod
    def get_task(task_id):
        task = TaskRepository.find_by_id(task_id)
        if task is None:
            return jsonify({"message":"Task not found"}), 404
        return jsonify({"task":task}), 200

    @staticmethod
    def update_task(task_id, data):
        task = TaskRepository.find_by_id(task_id)
        if task is None:
            return jsonify({"message":"Task not found"}), 404
        print(task["title"])
        task["title"] = data["title"]
        task["description"] = data["description"]
        task["date_updated"] = datetime.now()
        TaskRepository.update(task)
        return jsonify({"message":"Task updated","task":task}), 200

    @staticmethod
    def get_all_tasks():
        tasks = TaskRepository.find_all()
        return jsonify({"tasks":tasks}), 200

    @staticmethod
    def delete_task(task_id):
        TaskRepository.delete_by_id(task_id)
        return jsonify({"message": "Task deleted"}), 200

    @staticmethod
    def update_task_status(task_id, status_str):
        try:
            TaskStatusEnum[status_str]
        except KeyError:
            return jsonify({"message": "Invalid status value"}), 400
        task = TaskRepository.find_by_id(task_id)
        if task is None:
            return jsonify({"message":"Task not found"}), 404
        task["status"] = status_str
        task["date_updated"] = datetime.now()
        TaskRepository.update(task)
        return jsonify({"message":"Task status updated"}), 200
