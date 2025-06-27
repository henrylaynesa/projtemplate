from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config")
    db.init_app(app)

    with app.app_context():
        from . import models  # noqa: F401

        db.create_all()

    # Register blueprints here
    from .routes import main_bp

    app.register_blueprint(main_bp)

    return app
