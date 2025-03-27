from datetime import datetime

from flask import jsonify

from models.organization import Organization
from repositories.organization_repository import OrganizationRepository


class OrganizationService:

    @staticmethod
    def create_organization(data, user_id):
        organization = Organization(name=data["name"], description=data["description"],
                                    created_by=user_id, site_name=data["site_name"])
        if OrganizationRepository.find_by_site_name(organization.site_name) is None:
            saved_organization = OrganizationRepository.save(organization)
            return jsonify({"message": "Organization created", "organization": saved_organization}), 201
        else: return jsonify({"message": "Organization already exists"}), 400

    @staticmethod
    def edit_organization(organization_id, data, user_id):
        print(organization_id)
        print(data["site_name"])
        if "name" not in data and "description" not in data:
            return jsonify({"message": "Name or description missing"}), 400
        organization = OrganizationRepository.find_by_id_and_site_name(organization_id, data["site_name"])
        if organization is None:
            return jsonify({"message": "Organization not found"}), 404
        if "name" in data:
            organization["name"] = data["name"]
        if "description" in data:
            organization["description"] = data["description"]
        organization["date_updated"] = datetime.now()
        organization["updated_by"] = user_id
        OrganizationRepository.update(organization)
        return jsonify({"message": "Organization updated", "organization": organization}), 200

    @staticmethod
    def view_organization(organization_id):
        organization = OrganizationRepository.find_by_id(organization_id)
        if organization is None:
            return jsonify({"message": "Organization not found"}), 404
        return jsonify({"message": "Organization found", "organization": organization}), 200

    @staticmethod
    def delete_organization(org_id, site_name):
        organization = OrganizationRepository.find_by_id_and_site_name(org_id, site_name)
        if organization is None:
            return jsonify({"message": "Organization not found"}), 404
        OrganizationRepository.delete(org_id)
        return jsonify({"message": "Organization deleted"}), 200
