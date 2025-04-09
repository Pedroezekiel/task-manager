from models.organization import Organization
from serializers.organization_serializer import OrganizationSerializer
from extensions.database import mongo_tasks as mongo

class OrganizationRepository:

    @staticmethod
    def save(organization):
        serialized_organization = OrganizationSerializer.serialize(organization)
        organization = mongo.db.organizations.insert_one(serialized_organization)
        inserted_organization = mongo.db.organizations.find_one({"_id": organization.inserted_id})

        return OrganizationSerializer.deserialize(inserted_organization)

    @staticmethod
    def find_by_site_name(site_name):
        organizations = mongo.db.organizations.find_one({"site_name": site_name})
        print(organizations)
        if organizations is None:
            return None
        else: return OrganizationSerializer.deserialize(organizations)

    @staticmethod
    def find_by_id_and_site_name(org_id, site_name):
        organizations = mongo.db.organizations.find_one({"_id": org_id, "site_name": site_name})
        print(organizations)
        if organizations is None:
            return None
        else: return OrganizationSerializer.deserialize(organizations)

    @staticmethod
    def update(data: dict):
        mongo.db.organizations.update_one({"_id": data["id"]}, {"$set": data})

    @staticmethod
    def find_by_id(organization_id):
        organization = mongo.db.organizations.find_one({"_id": organization_id})
        if organization is None:
            return None
        else: return OrganizationSerializer.deserialize(organization)

    @staticmethod
    def delete(organization_id):
        mongo.db.organizations.delete_one({"_id": organization_id})

    @staticmethod
    def find_org_name_by_id(org_id):
        organizations = mongo.db.organizations.find_one({"_id": org_id})
        if organizations is None:
            return None
        else: return organizations["name"]

    @staticmethod
    def find_org_name_by_site_name(site_name):
        organizations = mongo.db.organizations.find_one({"site_name": site_name})
        if organizations is None:
            return None
        else: return organizations["name"]