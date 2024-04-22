from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
from config import Config

from app.api.v1.controllers.runbook_controller import bp as runbook_bp
from app.api.v1.controllers.history_controller import bp as history_bp

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    # Configuration and initialization code...

    app.register_blueprint(runbook_bp, url_prefix='/api/v1')
    app.register_blueprint(history_bp, url_prefix='/api/v1')

    return app