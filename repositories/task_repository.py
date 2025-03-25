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
    def find_by_id(task_id):
        task = mongo.db.tasks.find_one({"_id": task_id})
        if task is not None:
            return TaskSerializer.deserialize(task)
        else: return None

    @staticmethod
    def find_all():
        tasks = mongo.db.tasks.find()
        return [TaskSerializer.deserialize(task) for task in tasks]

    @staticmethod
    def delete_by_id(task_id):
        mongo.db.tasks.delete_one({"_id": task_id})



