import uuid
from datetime import datetime


class Organization:

    def __init__(self, name, description, created_by, site_name):
        self._id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.created_by = created_by
        self.updated_by = None
        self.site_name = site_name
        self.date_created = datetime.now()
        self.date_updated = None


    def get_id(self):
        return self._id
