from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from .config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(Config)
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    from .models import Usuario
    
    @login_manager.user_loader
    def get_user(usuario_id):
        return Usuario.query.get(usuario_id)

    from .tasks import task as tasks_blueprint
    app.register_blueprint(tasks_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app