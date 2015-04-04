import logging
import os
import sys
from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import flask.ext.script
import flask.ext.migrate
from sqlalchemy import create_engine

import pikka_bird_receiver.routes.statics


def create_app():
    app = Flask('pikka_bird_receiver')
    
    app.debug = (os.environ['LOG_LEVEL'] == 'DEBUG')
    app.db    = create_engine(os.environ['DATABASE_URI'])
    
    app.register_blueprint(pikka_bird_receiver.routes.statics.statics)
    
    __setup_logger(app.logger)
    __setup_db(app)
    
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

def __setup_db(app):
    auto_migrate = (int(os.environ['DATABASE_AUTO_MIGRATE']) == 1)
    
    db = SQLAlchemy(app)
    flask.ext.migrate.Migrate(app, db) # attach for Alembic
    
    if auto_migrate:
        app.logger.info('DATABASE AUTO-MIGRATING')
        
        with app.app_context():
            flask.ext.migrate.upgrade()

if __name__ == '__main__':
    app     = create_app()
    manager = create_manager(app)
    
    manager.run()
