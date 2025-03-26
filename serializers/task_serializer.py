from datetime import datetime

from enums.task_status import TaskStatusEnum


class TaskSerializer:
    @staticmethod
    def serialize(task):
        return {
            "_id": task.get_id(),
            "title": task.title,
            "description": task.description,
            "status": task.status.value if isinstance(task.status, TaskStatusEnum) else str(task.status),
            "created_at": task.created_at,
            "date_updated": task.date_updated,
            "user_id": task.user_id,
            "updated_by": task.updated_by
        }

    @staticmethod
    def deserialize(data: dict) -> dict:
        return {
            "_id": data["_id"],
            "title": data["title"],
            "description": data["description"],
            "status": data["status"],  # Assuming it's already a string in MongoDB
            "created_at": TaskSerializer.convert_datetime(data.get("created_at")),
            "data_created": TaskSerializer.convert_datetime(data.get("data_created")),
            "date_updated": TaskSerializer.convert_datetime(data.get("date_updated")),
            "updated_by": data["updated_by"]
        }

    @staticmethod
    def convert_datetime(value):
        if isinstance(value, str):
            return datetime.fromisoformat(value)
        return value