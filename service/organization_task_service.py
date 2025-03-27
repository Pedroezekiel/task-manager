from datetime import datetime

from flask import jsonify

from enums.task_status import TaskStatusEnum
from models.task import Task
from repositories.organization_repository import OrganizationRepository
from repositories.task_repository import TaskRepository
from service.task_service import TaskService


class OrganizationTaskService:

    @staticmethod
    def org_create_task(data, user_id):
        if OrganizationRepository.find_by_site_name(data["site_name"]) is None:
            return jsonify({"message": "Organization not found"}), 404
        task = Task(title=data["title"],description=data["description"], user_id=user_id, site_name=data["site_name"])
        saved_task = TaskRepository.save(task)
        return jsonify({"message":"Task created","task": saved_task}), 201

    @staticmethod
    def org_view_tasks(site_name, task_id):
        if OrganizationRepository.find_by_site_name(site_name) is None:
            return jsonify({"message": "Organization not found"}), 404
        task = TaskRepository.find_by_id_and_site_name(task_id, site_name)
        if task is None:
            return jsonify({"message": "Task not found"}), 404
        return jsonify({"task": task}), 200

    @staticmethod
    def org_view_all_tasks(site_name):
        if OrganizationRepository.find_by_site_name(site_name) is None:
            return jsonify({"message": "Organization not found"}), 404
        task = TaskRepository.find_all_by_site_name(site_name)
        if task is None:
            return jsonify({"message": "No task found"}), 404
        return jsonify({"task": task}), 200

    @staticmethod
    def org_edit_task(data, site_name, task_id, user_id):
        if OrganizationRepository.find_by_site_name(site_name) is None:
            return jsonify({"message": "Organization not found"}), 404
        if "title" not in data and "description" not in data:
            return jsonify({"message": "At least one field (title or description) must be provided"}), 400
        task = TaskRepository.find_by_id_and_site_name(task_id, site_name)
        if task is None:
            return jsonify({"message": "Task not found"}), 404
        task = TaskService.update_task_fields(task, data, user_id)
        TaskRepository.update(task)
        return jsonify({"message": "Task updated", "task": task}), 200

    @staticmethod
    def org_delete_task(site_name, task_id):
        if OrganizationRepository.find_by_site_name(site_name) is None:
            return jsonify({"message": "Organization not found"}), 404
        task = TaskRepository.find_by_id_and_site_name(task_id, site_name)
        if task is None:
            return jsonify({"message": "Task not found"}), 404
        TaskRepository.delete_by_id(task_id)
        return jsonify({"message": "Task deleted"}), 200

    @staticmethod
    def org_update_task_status(status_str, site_name, task_id, user_id):
        try:
            TaskStatusEnum[status_str]
        except KeyError:
            return jsonify({"message": "Invalid status value"}), 400
        if OrganizationRepository.find_by_site_name(site_name) is None:
            return jsonify({"message": "Organization not found"}), 404
        task = TaskRepository.find_by_id_and_site_name(task_id, site_name)
        if task is None:
            return jsonify({"message": "Task not found"}), 404
        task["status"] = status_str
        task["date_updated"] = datetime.now()
        TaskRepository.update(task)
        return jsonify({"message": "Task updated", "task": task}), 200
