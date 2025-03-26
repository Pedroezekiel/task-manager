from flask import Blueprint

from controllers.organization_controller import OrganizationController


class OrganizationRoutes(Blueprint):

    def __init__(self):
        super().__init__("organization_routes", __name__, url_prefix="/api/org")
        self.register_routes()

    def register_routes(self):
        print("===============================+++++++++++++++++++++")
        self.add_url_rule("/", view_func=OrganizationController.create_organization, methods=["POST"])

organization_routes = OrganizationRoutes()
