from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import flask.ext.script
import flask.ext.migrate


def create_manager(app):
    manager = flask.ext.script.Manager(app)
    manager.add_command('db', flask.ext.migrate.MigrateCommand)
    
    return manager


if __name__ == '__main__':
    app     = Flask('pikka_bird_server')
    manager = create_manager(app)
    
    db = SQLAlchemy(app)
    flask.ext.migrate.Migrate(app, db) # attach for Alembic
    
    manager.run()
