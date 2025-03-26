from models.organization import Organization
from serializers.organization_serializer import OrganizationSerializer
from extensions.database import mongo_organizations as mongo

class OrganizationRepository:

    @staticmethod
    def save(organization):
        serialized_organization = OrganizationSerializer.serialize(organization)
        mongo.db.organizations.insert_one(serialized_organization)
        return serialized_organization

    @staticmethod
    def find_by_site_name(site_name):
        organizations = mongo.db.organizations.find_one({"site_name": site_name})
        print(organizations)
        if organizations is None:
            return None
        else: return OrganizationSerializer.deserialize(organizations)

    @staticmethod
    def find_by_id_and_site_name(org_id, site_name):
        organizations = mongo.db.organizations.find_one({"id": org_id, "site_name": site_name})
        if organizations is None:
            return None
        else: OrganizationSerializer.deserialize(organizations)

    @staticmethod
    def update(data: dict):
        mongo.db.organizations.update_one({"id": data["id"]}, {"$set": data})