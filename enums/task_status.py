from enum import Enum


class TaskStatusEnum(Enum):
    TO_DO = "to_do"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
