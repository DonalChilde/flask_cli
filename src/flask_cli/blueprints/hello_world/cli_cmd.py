from flask_cli.blueprints.cli_base.bp_config import bp
from flask_cli.blueprints.cli_base.cli_cmd import pass_environment
import click


@bp.cli.group("hello_world", help="A collection of commands related to hello_world")
@pass_environment
def hello_world(ctx):
    pass


@hello_world.command("greet")
@click.argument("name")
@pass_environment
def greet(ctx, name):
    ctx.log(f"Hello World! --from {name}")
