from flask import Flask, render_template, Blueprint
from app.database import db

from .error_handler import page_not_found
import app.routes as routes
import os


# create the app & initialise the configurations.
# default config given is dev.cfg
def create_app():
    # the flask object
    server = Flask(__name__)
    load_config(server)
    register_extension(server)
    register_blueprints(server)
    print("From server %s" % (server.config['ENVBITCH']))

    server.register_error_handler(404, page_not_found)

    return server


def register_blueprints(server):
    """registers all the blueprints in the routes modules"""
    for blueprint in vars(routes).values():
        if isinstance(blueprint, Blueprint):

            server.register_blueprint(blueprint, url_prefix='/api')


def register_extension(server):
    """registers the extensions"""
    db.init_app(server)


def load_config(server):
    """loads configuration for current enviornment (FLASK_ENV) from OS

      `export FLASK_ENV=development`
    """

    flask_env = "development"
    print("Loading ''%s'' configuration..." % (flask_env), flush=True)

    if flask_env == "development":
        server.config.from_pyfile('dev.cfg')
    else:
        server.config.from_pyfile('test.cfg')
