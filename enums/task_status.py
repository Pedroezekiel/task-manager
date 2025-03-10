import enum


class TaskStatusEnum(enum.Enum):
    TO_DO = "to_do"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
