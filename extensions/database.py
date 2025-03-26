from flask_pymongo import PyMongo

mongo_tasks = PyMongo()
mongo_users = PyMongo()
mongo_organizations = PyMongo()
mongo_organization_members = PyMongo()

def init_db(app):
    mongo_tasks.init_app(app, uri=app.config["MONGO_URI_TASKS"])
    mongo_users.init_app(app, uri=app.config["MONGO_URI_USERS"])
    mongo_organizations.init_app(app, uri=app.config["MONGO_URI_ORG"])
    mongo_organization_members.init_app(app, uri=app.config["MONGO_URI_ORG_MEMBER"])

    with app.app_context():
        print(f"Databases initialized: {mongo_tasks.db.name}, "
              f"{mongo_users.db.name}, {mongo_organizations.db.name}, {mongo_organization_members.db.name}")
