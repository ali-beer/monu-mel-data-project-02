from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask_restful import Api

app = Flask(__name__)
db = SQLAlchemy()
api = Api()


def create_app(config_class=Config, api=api, db=db):
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initializing API routes
    from flaskapp.api.routes import initialise_api_routes
    initialise_api_routes(api)

    # Initiating app components

    db.init_app(app)
    api.init_app(app)

    Migrate(app, db)

    from flaskapp.main.routes import main
    from flaskapp.errors.handlers import errors
    from flaskapp.api.routes import api_bp

    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(api_bp)

    return app


app = create_app()
