"""Entry point for flask app.

derived from 
     https://github.com/karec/cookiecutter-flask-restful/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/%7B%7Bcookiecutter.app_name%7D%7D/app.py

    """

from flask import Flask


from flask_cli.blueprints import hello_world, cli_base
from flask_cli.blueprints.cli_base.cli_cmd import app_group


def create_app(testing=False, cli=False):
    """Application factory, used to create application
    """
    app = Flask(__name__)
    app.config.from_object("flask_cli.config")

    if testing is True:
        app.config["TESTING"] = True

    configure_extensions(app, cli)
    configure_apispec(app)
    register_blueprints(app)
    app.cli.add_command(app_group)
    return app


def configure_extensions(app, cli):
    """configure flask extensions
    """
    pass


def configure_apispec(app):
    """Configure APISpec for swagger support
    """
    pass


def register_blueprints(app):
    """register all blueprints for application
    """
    app.register_blueprint(hello_world.bp_config.bp)
    app.register_blueprint(cli_base.bp_config.bp)
