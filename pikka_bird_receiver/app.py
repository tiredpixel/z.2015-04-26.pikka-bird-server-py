import logging
import os
import sys

from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import flask.ext.script
import flask.ext.migrate

from pikka_bird_receiver.database import db_session
import pikka_bird_receiver.routes.statics


def create_app():
    app = Flask('pikka_bird_receiver')
    
    app.debug = (os.environ['LOG_LEVEL'] == 'DEBUG')
    
    app.register_blueprint(pikka_bird_receiver.routes.statics.statics)
    
    __setup_logger(app.logger)
    
    return app

def create_manager(app):
    manager = flask.ext.script.Manager(app)
    manager.add_command('db', flask.ext.migrate.MigrateCommand)
    
    return manager

def __setup_logger(logger):
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s -- %(name)s: %(message)s')
    
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    
    logger.setLevel(os.environ['LOG_LEVEL'])
    logger.addHandler(handler)


if __name__ == '__main__':
    app     = create_app()
    manager = create_manager(app)
    
    db = SQLAlchemy(app)
    flask.ext.migrate.Migrate(app, db) # attach for Alembic
    
    manager.run()
