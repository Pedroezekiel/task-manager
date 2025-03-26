import datetime
import uuid
from enums.task_status import TaskStatusEnum

class Task:

    def __init__(self, title, description,user_id, status=TaskStatusEnum.TO_DO):
        self._id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.status = status
        self.created_at = datetime.datetime.now()
        self.date_updated = None
        self.updated_by = None
        self.user_id = user_id

    def get_id(self):
        return self._id