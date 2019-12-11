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

        from blast.blueprints import auth, errors, landing, mainsite, profile
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(landing.welcome_bp)
        app.register_blueprint(mainsite.main_bp)
        app.register_blueprint(profile.profile_bp)
        app.register_blueprint(errors.err)

        from blast.models import User
        @loginManager.user_loader
        def load_user(id):
            return User.query.get(int(id))

    return app


from blast import models
