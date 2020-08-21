from flask_cli.blueprints.cli_base.bp_config import bp


@bp.route("/")
def cli_base():
    return "Example cli_base route."
