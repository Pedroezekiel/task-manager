from flask import Blueprint

from controllers.organization_controller import OrganizationController
from controllers.organization_member_controller import OrganizationMemberController


class OrganizationRoutes(Blueprint):

    def __init__(self):
        super().__init__("organization_routes", __name__, url_prefix="/api/org")
        self.register_routes()

    def register_routes(self):
        print("===============================+++++++++++++++++++++")
        self.add_url_rule("/", view_func=OrganizationController.create_organization, methods=["POST"])
        self.add_url_rule("/<org_id>", view_func=OrganizationController.edit_organization, methods=["PUT"])
        self.add_url_rule("/<org_id>", view_func=OrganizationController.view_organization, methods=["GET"])
        self.add_url_rule("/<site_name>/<org_id>", view_func=OrganizationController.delete_organization, methods=["DELETE"])
        self.add_url_rule("/tasks", view_func=OrganizationController.organization_create_task, methods=["POST"])
        self.add_url_rule("/tasks/<task_id>/<site_name>", view_func=OrganizationController.organization_edit_task, methods=["PUT"])
        self.add_url_rule("/tasks/<task_id>/<site_name>", view_func=OrganizationController.organization_view_task, methods=["GET"])
        self.add_url_rule("/tasks/<site_name>", view_func=OrganizationController.organization_view_all_tasks, methods=["GET"])
        self.add_url_rule("/tasks/<task_id>/<site_name>", view_func=OrganizationController.organization_delete_task, methods=["DELETE"])
        self.add_url_rule("/member/", view_func=OrganizationMemberController.add_organization_member, methods=["POST"])
        self.add_url_rule("/member/<site_name>", view_func=OrganizationMemberController.member_join_organization, methods=["POST"])
        self.add_url_rule("/member/<site_name>", view_func=OrganizationMemberController.view_all_organization_members, methods=["GET"])
        self.add_url_rule("/member/<site_name>", view_func= OrganizationMemberController.member_view_tasks, methods=["GET"])
        self.add_url_rule("/<status_str>/<site_name>/<task_id>", view_func=OrganizationController.organization_update_task_status, methods=["PUT"])
        self.add_url_rule("<site_name>/<task_id>/<member_id>", view_func=OrganizationController.organization_assign_task, methods=["PATCH"])

organization_routes = OrganizationRoutes()