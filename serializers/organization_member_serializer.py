from repositories.organization_repository import OrganizationRepository
from repositories.user_repository import UserRepository
from utils.date_time_utils import DateTimeUtils

class OrganizationMemberSerializer:

    @staticmethod
    def serialize(organization_member):
        user = UserRepository.find_by_id(organization_member.user_id)
        organization_name = OrganizationRepository.find_org_name_by_id(organization_member.organization_id)
        return {
            "id": organization_member.get_id(),
            "userName": user["name"],
            "userEmail": user["email"],
            "role": organization_member.role,
            "dateJoined": DateTimeUtils.convert_datetime(organization_member.date_joined),
            "siteName": organization_member.site_name,
            "organizationName": organization_name
        }

    @staticmethod
    def deserialize(serialized_data):
        return {
            "id": serialized_data["id"],
            "userName": serialized_data["userName"],
            "userEmail": serialized_data["userEmail"],
            "role": serialized_data["role"],
            "dateJoined": DateTimeUtils.convert_datetime(serialized_data["dateJoined"]),
            "siteName": serialized_data["siteName"],
            "organizationName": serialized_data["organizationName"]
        }