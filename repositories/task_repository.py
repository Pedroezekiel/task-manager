from bson import ObjectId
from bson.errors import InvalidId

from models.task import Task
from extensions.database import mongo
from serializers.task_serializer import TaskSerializer


class TaskRepository:

    @staticmethod
    def save_or_update(task: Task):
        serialized_task = TaskSerializer.serialize(task)
        mongo.db.tasks.update_one({"id": task.id}, {"$set": serialized_task}, upsert=True)

    @staticmethod
    def find_by_id(task_id):
        print(f"===============-  {task_id}")

        try:
            # If task_id is a valid ObjectId, use it
            obj_id = ObjectId(task_id)
        except:
            # Otherwise, assume it's a UUID stored as a string
            obj_id = task_id

        print("obj_id:", obj_id)
        task = mongo.db.tasks.find_one({"id": obj_id})
        print("task:", task)

        if task is None:
            return {"error": "Task not found"}, 404

        return task

    @staticmethod
    def find_all():
        tasks = mongo.db.tasks.find()
        return [TaskSerializer.serialize(task) for task in tasks]

    @staticmethod
    def delete_by_id(task_id):
        task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
        if task is None:
            return {"error": "Task not found"}, 404
        mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})



