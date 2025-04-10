from repositories.organization_repository import OrganizationRepository
from extensions.database import mongo_tasks as mongo
from serializers.organization_member_serializer import OrganizationMemberSerializer


class OrganizationMemberRepository:

    @staticmethod
    def save(organization_member):
        serialized_org_member = OrganizationMemberSerializer.serialize(organization_member)
        mongo.db.organization_members.insert_one(serialized_org_member)
        return serialized_org_member

    @staticmethod
    def find_by_site_name_and_user_id(site_name, user_id):
        organization_member = mongo.db.organization_members.find_one({"site_name": site_name, "user_id": user_id})
        if organization_member:
            return OrganizationMemberSerializer.deserialize(organization_member)
        else: return None

    @staticmethod
    def find_by_site_name_and_user_email(site_name, user_email):
        organization_member = mongo.db.organization_members.find_one({"site_name": site_name, "user_email": user_email})
        print(organization_member)
        if organization_member:
            return OrganizationMemberSerializer.deserialize(organization_member)
        else: return None

    @staticmethod
    def find_all_by_site_name(site_name):
        organization_members = mongo.db.organization_members.find({"site_name": site_name})
        return [OrganizationMemberSerializer.deserialize(organization_member)
                for organization_member in organization_members]