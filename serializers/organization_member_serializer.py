from repositories.organization_repository import OrganizationRepository
from repositories.user_repository import UserRepository
from utils.date_time_utils import DateTimeUtils

class OrganizationMemberSerializer:

    @staticmethod
    def serialize(organization_member):
        user = UserRepository.find_by_id(organization_member.user_id)
        organization_name = OrganizationRepository.find_org_name_by_site_name(organization_member.site_name)
        return {
            "id": organization_member.get_id(),
            "user_name": user["name"],
            "user_email": user["email"],
            "role": organization_member.role.value,
            "date_joined": DateTimeUtils.convert_datetime(organization_member.date_joined),
            "site_name": organization_member.site_name,
            "organization_name": organization_name
        }

    @staticmethod
    def deserialize(serialized_data):
        return {
            "id": serialized_data["id"],
            "user_name": serialized_data["user_name"],
            "user_email": serialized_data["user_email"],
            "role": serialized_data["role"],
            "date_joined": DateTimeUtils.convert_datetime(serialized_data["date_joined"]),
            "site_name": serialized_data["site_name"],
            "organization_name": serialized_data["organization_name"]
        }