from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from service.organization_service import OrganizationService

class OrganizationController:

    @staticmethod
    @jwt_required()
    def create_organization():
        user_id = get_jwt_identity()
        data = request.get_json()
        return OrganizationService.create_organization(data, user_id)

    @staticmethod
    @jwt_required()
    def edit_organization(org_id):
        user_id = get_jwt_identity()
        data = request.get_json()
        return OrganizationService.edit_organization(org_id, data, user_id)

    @staticmethod
    @jwt_required()
    def view_organization(org_id):
        return OrganizationService.view_organization(org_id)

    @staticmethod
    @jwt_required()
    def delete_organization(org_id, site_name):
        return OrganizationService.delete_organization(org_id, site_name)