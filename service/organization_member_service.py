from flask import jsonify

from enums.member_role_status import MemberRoleEnum
from models.organization_member import OrganizationMember
from repositories.organization_member_repository import OrganizationMemberRepository
from repositories.user_repository import UserRepository
from repositories.organization_repository import OrganizationRepository

class OrganizationMemberService:

    @staticmethod
    def add_member_to_organization(data, user_id):
        user = UserRepository.find_by_id(user_id)
        organization = OrganizationMemberRepository.find_by_site_name_and_user_email(data["site_name"], user["email"])
        if organization is None:
            return jsonify({"error":"User is not authorized"}), 401
        user = UserRepository.find_by_email(data["email"])
        if user is None:
            return jsonify({"error":"User is not found"}), 401
        org_member = OrganizationMember(user_id=user.get_id(), org_id=organization["id"], site_name=organization["site_name"])
        if data["role"] in data:
            try:
                MemberRoleEnum[data["role"]]
            except KeyError:
                return jsonify({"message": "Invalid status value"}), 400
            org_member.role = MemberRoleEnum[data["role"]]
        saved_org = OrganizationMemberRepository.save(org_member)
        return jsonify(saved_org), 200

    @staticmethod
    def member_join_organization(user_id, site_name):
        if OrganizationMemberRepository.find_by_site_name_and_user_id(site_name, user_id):
            return jsonify({"error":"member already in organization"}), 401
        organization = OrganizationRepository.find_by_site_name(site_name)
        org_member = OrganizationMember(user_id=user_id, org_id=organization["id"], site_name=organization["site_name"])
        saved_org = OrganizationMemberRepository.save(org_member)
        return jsonify(saved_org), 200

    @staticmethod
    def view_organization_members(user_id, site_name):
        user = UserRepository.find_by_id(user_id)
        if OrganizationMemberRepository.find_by_site_name_and_user_email(site_name, user["email"]) is None:
            return jsonify({"error":"User is not in this organization"}), 401
        organizations = OrganizationMemberRepository.find_all_by_site_name(site_name)
        return jsonify({"organizations": organizations}), 200
