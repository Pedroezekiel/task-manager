from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

from service.organization_member_service import OrganizationMemberService

class OrganizationMemberController:

    @staticmethod
    @jwt_required()
    def add_organization_member():
        data=request.get_json()
        user_id = get_jwt_identity()
        return OrganizationMemberService.add_member_to_organization(data, user_id)

    @staticmethod
    @jwt_required()
    def member_join_organization(site_name):
        user_id = get_jwt_identity()
        return OrganizationMemberService.member_join_organization(user_id, site_name)

    @staticmethod
    @jwt_required()
    def view_all_organization_members(site_name):
        user_id = get_jwt_identity()
        return OrganizationMemberService.view_organization_members(user_id, site_name)
