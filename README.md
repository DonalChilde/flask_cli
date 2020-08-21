# flask_cli

Examples of different ways to make a custom cli in Flask

## [Flask blueprint.cli](https://flask.palletsprojects.com/en/1.1.x/cli/#registering-commands-with-blueprints)

In addition to their usefulness in breaking up large projects in to manageable chunks, Flask blueprints also provide an easy way to add Click cli commands and groups to the flask terminal command. For instance, in addition to the standard flask cli commands of

```bash
flask run
flask routes
flask shell
```

you might make additional commands like

```bash
flask app init_db
flask do_some_work
flask hello_world --name Bob
```

See the branch labeled blueprint_cli for examples.

Pros

- Easy to use built in functionality.
- Does not require the installation of a separate cli app.
- Automatic discovery of commands, so long as the containing module is imported somewhere, e.g. in the package `__init__.py`
- Easy to divide areas of responsibility using existing Blueprint structure.
- Automatic wrapping of commands with [@with_appcontext](https://flask.palletsprojects.com/en/1.1.x/cli/#application-context) so that `current_app` is available inside your custom commands.

Cons

- Beyond custom names, you are unable to customize the top level group. This means no help description for the top group, or options/arguments that can be passed to child commands.
- No bash completion.

## [Manually adding commands to flask](https://flask.palletsprojects.com/en/1.1.x/cli/#application-context)

It is also possible to manually add Click commands and groups to the flask terminal command. In the function where you create your Flask app instance, use `app.cli.addcommand()` to add the Click command or group.

```python
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
    # this is the line that adds a Click group to the flask cli.
    app.cli.add_command(app_group)
    return app
```

This method requires an extra step to make sure that current_app is available inside commands. Command functions must be decorated with [with_appcontext](https://flask.palletsprojects.com/en/1.1.x/cli/#application-context).

```python
import click
from flask import current_app
from flask.cli import with_appcontext

@app_group.command("info", help="an example command in the flask.app group.")
@with_appcontext
@pass_environment
def info_b(ctx):
    ctx.log("App info:", current_app, f"environment: {current_app.config.get('ENV')}")
```

See the branch labeled manual_cli for examples.

Pros

- Only one extra statement required over the blueprint.cli method.
- Does not require the installation of a separate cli app.
- Automatic discovery of commands that are children of a registered Click group, so long as the containing module is imported somewhere, e.g. in the package `__init__.py`
- Easy to divide areas of responsibility using existing Blueprint structure.
- Control over the top-level cli group. Can add custom help, and options/arguments.

Cons

- You must add `@with_appcontext` to each function that requires the use of `current_app`
- No bash completion.
- Top level commands and groups must be manually registered with `app.cli.addcommand`

## [Custom Scripts](https://flask.palletsprojects.com/en/1.1.x/cli/#custom-scripts)

This is the route taken by most tutorials I have seen. With the exception of bash completion, manually adding commands to `app.cli` seems the better choice.

Pros

- Bash completion
- Control over the top-level cli group. Can add custom help, and options/arguments.

Cons

- Must create app when app context needed?
- TODO - see if this works. You must add `@with_appcontext` to each function that requires the use of `current_app`
- must define entry point in setup.py/cfg

## [Plugins](https://flask.palletsprojects.com/en/1.1.x/cli/#plugins)

Might be useful if cli is developed separate from flask project? Needs its own setup.py.
