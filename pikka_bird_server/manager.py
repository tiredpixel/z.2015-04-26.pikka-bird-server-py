import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import flask.ext.script
import flask.ext.migrate


def create_manager(app):
    manager = flask.ext.script.Manager(app)
    manager.add_command('db', flask.ext.migrate.MigrateCommand)
    
    return manager

def run():
    app     = Flask('pikka_bird_server')
    manager = create_manager(app)
    
    dir_migrations = os.path.join(os.path.dirname(__file__), 'migrations')
    
    db = SQLAlchemy(app)
    flask.ext.migrate.Migrate(app, db, directory=dir_migrations)
    
    manager.run()


if __name__ == '__main__':
    run()
