from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import reqparse, Api

# setup db
db = SQLAlchemy()

def create_app(**config_overrides):
    app = Flask(__name__)

    # set the main api handler
    api = Api(app)

    # Load config
    app.config.from_pyfile('settings.py')

    # apply overrides for tests
    app.config.update(config_overrides)

    # initialize db
    db.init_app(app)
    migrate = Migrate(app, db)

    # set routes
    from pet.resources import PetList
    api.add_resource(PetList, '/pets')

    return app
