from flask_pymongo import PyMongo

mongo_tasks = PyMongo()
mongo_users = PyMongo()

def init_db(app):
    mongo_tasks.init_app(app, uri=app.config["MONGO_URI_TASKS"])
    mongo_users.init_app(app, uri=app.config["MONGO_URI_USERS"])

    with app.app_context():
        print(f"Databases initialized: {mongo_tasks.db.name}, {mongo_users.db.name}")
