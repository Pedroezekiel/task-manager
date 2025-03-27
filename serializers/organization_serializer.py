from repositories.user_repository import UserRepository
from utils.date_time_utils import DateTimeUtils


class OrganizationSerializer:

    @staticmethod
    def serialize(organization):
        return {
            "_id": organization.get_id(),
            "name": organization.name,
            "created_by": organization.created_by,
            "description": organization.description,
            "date_created": organization.date_created,
            "date_updated": organization.date_updated,
            "updated_by": organization.updated_by,
            "site_name": organization.site_name,
        }

    @staticmethod
    def deserialize(data):
        print(data["name"])
        return {
            "id": data["_id"],
            "name": data["name"],
            "site_name": data["site_name"],
            "description": data["description"],
            "date_created": DateTimeUtils.convert_datetime(data["date_created"]),
            "date_updated": DateTimeUtils.convert_datetime(data["date_updated"]),
            "created_by": data["created_by"],
            "updated_by": data["updated_by"]
        }