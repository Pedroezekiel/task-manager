from flask import Blueprint

from controllers.organization_controller import OrganizationController


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

organization_routes = OrganizationRoutes()
