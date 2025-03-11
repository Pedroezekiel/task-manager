from flask import jsonify

from models.task import Task
from repositories.task_repository import TaskRepository
from serializers.task_serializer import TaskSerializer


class TaskService:

    @staticmethod
    def create_task(data):
        task = Task(title=data["title"],description=data["description"])
        TaskRepository.save_or_update(task)
        return jsonify({"message":"Task created","task":TaskSerializer.serialize(task)}), 201

    @staticmethod
    def get_task(task_id):
        task = TaskRepository.find_by_id(task_id)
        return jsonify({"task":task}), 200
