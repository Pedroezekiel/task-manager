from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from service.organization_service import OrganizationService
from service.organization_task_service import OrganizationTaskService

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

    @staticmethod
    @jwt_required()
    def organization_create_task():
        data = request.get_json()
        user_id = get_jwt_identity()
        return OrganizationTaskService.org_create_task(data, user_id)

    @staticmethod
    @jwt_required()
    def organization_edit_task(task_id, site_name):
        user_id = get_jwt_identity()
        data = request.get_json()
        return OrganizationTaskService.org_edit_task(data, site_name, task_id, user_id)

    @staticmethod
    @jwt_required()
    def organization_view_task(task_id,site_name):
        return OrganizationTaskService.org_view_tasks(site_name,task_id)

    @staticmethod
    @jwt_required()
    def organization_view_all_tasks(site_name):
        return OrganizationTaskService.org_view_all_tasks(site_name)

    @staticmethod
    @jwt_required()
    def organization_edit_task(task_id, site_name):
        data = request.get_json()
        user_id = get_jwt_identity()
        return OrganizationTaskService.org_edit_task(data,site_name,task_id,user_id)

    @staticmethod
    @jwt_required()
    def organization_delete_task(site_name, task_id):
        return OrganizationTaskService.org_delete_task(site_name,task_id)