from flask import Blueprint

bp = Blueprint("cli_base", __name__, cli_group="app", url_prefix="/cli_base")
