from typing import Any

import click
from flask import current_app, g
from flask.cli import with_appcontext
from simplekv.fs import FilesystemStore


def get_db() -> FilesystemStore:
    if 'db' not in g:
        g.db = FilesystemStore(current_app.config['DATABASE'])
    return g.db


def init_db() -> None:
    get_db()


@click.command('init-db')
@with_appcontext
def init_db_command() -> None:
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app: Any) -> None:
    """Register database functions with the Flask app."""
    app.cli.add_command(init_db_command)
