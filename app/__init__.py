from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(Config)
    db.init_app(app)

    from .tasks import task as tasks_blueprint
    app.register_blueprint(tasks_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app