from flask import Flask
from config import Config
from extensions.database import init_db
from routes.task_routes import task_routes
from routes.user_routes import user_routes
app = Flask(__name__)
app.config.from_object(Config)
init_db(app)

app.register_blueprint(task_routes)
app.register_blueprint(user_routes)


if __name__ == '__main__':
    app.run(debug=True)

