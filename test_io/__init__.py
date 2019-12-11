from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


loginManager = LoginManager()
loginManager.login_view = 'auth.login'
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        loginManager.init_app(app)
        db.init_app(app)
        migrate.init_app(app, db)

        from blast.blueprints.auth import auth_bp
        app.register_blueprint(auth_bp)
        from blast.blueprints.landing import welcome_bp
        app.register_blueprint(welcome_bp)
        from blast.blueprints.mainsite import main_bp
        app.register_blueprint(main_bp)
        from blast.blueprints.profile import profile_bp
        app.register_blueprint(profile_bp)
        from blast.blueprints.errors import err
        app.register_blueprint(err)


    return app

from blast import models

