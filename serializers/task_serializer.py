from datetime import datetime

from enums.task_status import TaskStatusEnum


class TaskSerializer:
    @staticmethod
    def serialize(task):
        """Convert Task object to a dictionary for MongoDB storage."""
        # Debugging to check what is being stored
        print(f"DEBUG - task.status before serialization: {task.status}, type: {type(task.status)}")

        # Extract correct status value
        if isinstance(task.status, tuple):
            task.status = task.status[0]  # Unpack tuple

        return {
            "id": str(task.id),
            "title": task.title,
            "description": task.description,
            "status": task.status.value if isinstance(task.status, TaskStatusEnum) else str(task.status),
            "created_at": task.created_at.isoformat() if isinstance(task.created_at, datetime) else None,
        }
