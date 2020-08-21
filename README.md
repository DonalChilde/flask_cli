# flask_cli

Examples of different ways to make a custom cli in Flask

## Flask blueprints

In addition to their usefulness in breaking up large projects in to manageable chunks, Flask blueprints also provide an easy way to add click cli commands and groups to the flask terminal command. For instance, in addition to the standard flask cli commands of

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
- Automatic discovery of commands, so long as the containing module is imported.
- Easy to divide areas of responsibility using existing Blueprint structure.
- Automatic wrapping of commands with with_app_context so that current_app is available inside your custom commands.

Cons

- Beyond custom names, you are unable to customize the top level group. This means no help description for the top group.

## Manually adding commands to flask

## External cli program
