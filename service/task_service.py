from datetime import datetime

from flask import jsonify

from enums.task_status import TaskStatusEnum
from models.task import Task
from repositories.task_repository import TaskRepository


class TaskService:

    @staticmethod
    def create_task(data, user_id):
        task = Task(title=data["title"],description=data["description"], user_id=user_id)
        saved_task = TaskRepository.save(task)
        return jsonify({"message":"Task created","task": saved_task}), 201

    @staticmethod
    def search_tasks(user_id, query):
        tasks = TaskRepository.search_tasks(user_id, query)
        return jsonify({"tasks": tasks}), 200

    @staticmethod
    def get_task(task_id, user_id):
        task = TaskRepository.find_by_id(task_id, user_id)
        if task is None:
            return jsonify({"message":"Task not found"}), 404
        return jsonify({"task":task}), 200

    @staticmethod
    def update_task_fields(task, data, user_id):
        """Updates task fields if present in the data dictionary."""
        updated_fields = ["title", "description"]

        for field in updated_fields:
            if field in data:
                task[field] = data[field]

        task["date_updated"] = datetime.now()
        task["updated_by"] = user_id

        return task

    @staticmethod
    def update_task(task_id, data, user_id):
        if "title" not in data and "description" not in data:
            return jsonify({"message": "At least one field (title or description) must be provided"}), 400
        task = TaskRepository.find_by_id(task_id, user_id)
        if task is None:
            return jsonify({"message":"Task not found"}), 404
        print(task["title"])
        task = TaskService.update_task_fields(task, data, user_id)
        TaskRepository.update(task)
        return jsonify({"message":"Task updated","task":task}), 200

    @staticmethod
    def get_all_tasks(user_id):
        tasks = TaskRepository.find_all(user_id)
        if tasks is None:
            return jsonify({"message":"No task found"}), 404
        return jsonify({"tasks":tasks}), 200

    @staticmethod
    def delete_task(task_id, user_id):
        task = TaskRepository.find_by_id(task_id, user_id)
        TaskRepository.delete_by_id(task["_id"])
        return jsonify({"message": "Task deleted"}), 200

    @staticmethod
    def update_task_status(task_id, status_str, user_id):
        try:
            TaskStatusEnum[status_str]
        except KeyError:
            return jsonify({"message": "Invalid status value"}), 400
        task = TaskRepository.find_by_id(task_id, user_id)
        if task is None:
            return jsonify({"message":"Task not found"}), 404
        task["status"] = TaskStatusEnum[status_str].value
        task["date_updated"] = datetime.now()
        TaskRepository.update(task)
        return jsonify({"message":"Task status updated"}), 200

    @staticmethod
    def filter_task_by_status(status_str, user_id):
        try:
            TaskStatusEnum[status_str]
        except KeyError:
            return jsonify({"message": "Invalid status value"}), 400
        tasks = TaskRepository.find_all_by_status(user_id, TaskStatusEnum[status_str].value)
        if tasks is None:
            return jsonify({"message":"No tasks found"}), 404
        return jsonify({"tasks":tasks}), 200
