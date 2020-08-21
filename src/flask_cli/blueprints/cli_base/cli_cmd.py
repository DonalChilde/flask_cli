import sys
from itertools import chain

import click
from flask import current_app
from flask.cli import with_appcontext

from flask_cli.blueprints.cli_base.bp_config import bp


class Environment:
    def __init__(self):
        self.verbose = False

    def log(self, msg, *args):
        """Logs a message to stderr."""
        output = msg
        if args:
            # msg %= args
            msg_iter = chain((msg,), map(str, args))
            output = "\n\t".join(msg_iter)
        click.echo(output, file=sys.stderr)

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)


pass_environment = click.make_pass_decorator(Environment, ensure=True)


###### Blueprint Method #########


@bp.cli.command("info", help="an example command in the flask.app group.")
@with_appcontext
@pass_environment
def info(ctx):
    ctx.log("App info:", current_app, f"environment: {current_app.config.get('ENV')}")


@bp.cli.group("sub_group", help="a sub-group in the flask.app group.")
@click.option("-v", "--verbose", is_flag=True, help="Enables verbose mode.")
@pass_environment
def sub_group(ctx, verbose):
    ctx.verbose = verbose


@sub_group.command("command_1", help="A command attatched to the sub_group group.")
@pass_environment
def command_1(ctx):
    ctx.log("A log message.")
    ctx.vlog("A verbose log message.")
