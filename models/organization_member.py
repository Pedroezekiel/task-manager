import uuid
from datetime import datetime

from enums.member_role_status import MemberRoleEnum


class OrganizationMember:

    def __init__(self, user_id, org_id, site_name, role=MemberRoleEnum.MEMBER):
        self._id = str(uuid.uuid4())
        self.user_id = user_id
        self.org_id = org_id
        self.role = role
        self.date_joined = datetime.now()
        self.site_name = site_name