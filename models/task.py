import datetime
import uuid
from enums.task_status import TaskStatusEnum

class Task:

    def __init__(self, title, description, status=TaskStatusEnum.TO_DO):
        self._id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.status = status
        self.created_at = datetime.datetime.now()
        self.date_completed = None
        self.date_updated = None

    def get_id(self):
        return self._id