from flask import Flask

from config import Config
from extensions.database import init_db
from extensions.jwt import jwt,bcrypt
from routes.task_routes import task_routes
from routes.user_routes import user_routes
from routes.organization_routes import organization_routes
app = Flask(__name__)
app.config.from_object(Config)
init_db(app)
jwt.init_app(app)
bcrypt.init_app(app)

app.register_blueprint(task_routes)
app.register_blueprint(user_routes)
app.register_blueprint(organization_routes)


if __name__ == '__main__':
    app.run(debug=True)

