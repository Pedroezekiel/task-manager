from models import task
from models.task import Task
from extensions.database import mongo_tasks as mongo
from serializers.task_serializer import TaskSerializer


class TaskRepository:

    @staticmethod
    def save(task: Task):
        serialized_task = TaskSerializer.serialize(task)
        mongo.db.tasks.insert_one(serialized_task)
        return serialized_task

    @staticmethod
    def update(data: dict):
        mongo.db.tasks.update_one({"_id": data["_id"]}, {"$set": data})

    @staticmethod
    def find_by_id(task_id, user_id):
        task = mongo.db.tasks.find_one({"_id": task_id, "user_id": user_id})
        if task is not None:
            return TaskSerializer.deserialize(task)
        else: return None

    @staticmethod
    def find_all(user_id):
        tasks = mongo.db.tasks.find({"user_id":user_id})
        if tasks is None:
            return None
        else: return [TaskSerializer.deserialize(task) for task in tasks]

    @staticmethod
    def find_all_by_status(user_id, status):
        tasks = mongo.db.tasks.find({"user_id": user_id, "status": status})
        if tasks is None:
            return None
        else: return [TaskSerializer.deserialize(task) for task in tasks]

    @staticmethod
    def delete_by_id(task_id):
        mongo.db.tasks.delete_one({"_id": task_id})

    @staticmethod
    def find_by_id_and_site_name(task_id, site_name):
        task = mongo.db.tasks.find_one({"_id": task_id, "site_name": site_name})
        if task is not None:
            return TaskSerializer.deserialize(task)
        else: return None

    @staticmethod
    def find_all_by_site_name(site_name):
        tasks = mongo.db.tasks.find({"site_name": site_name})
        print(tasks,"=======================================")
        if tasks is None:
            return None
        return [TaskSerializer.deserialize(task) for task in tasks]

    @staticmethod
    def delete_all_by_site_name(site_name):
        result = mongo.db.tasks.delete_many({"site_name": site_name})
        print(f"Deleted {result.deleted_count} documents.")

    @staticmethod
    def find_all_by_site_name_and_user_id(site_name, user_id):
        tasks = mongo.db.tasks.find({"site_name": site_name, "user_id": user_id})
        if tasks is None:
            return None
        return [TaskSerializer.deserialize(task) for task in tasks]

