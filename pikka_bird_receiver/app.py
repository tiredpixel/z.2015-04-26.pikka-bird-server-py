import os
from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from sqlalchemy import create_engine

import pikka_bird_receiver.routes.statics


def create_app():
    app = Flask('pikka_bird_receiver')
    app.debug = (int(os.environ['DEBUG']) == 1)
    
    app.db = create_engine(os.environ['DATABASE_URI'])
    
    app.register_blueprint(pikka_bird_receiver.routes.statics.statics)
    
    return app

def create_manager(app):
    db = SQLAlchemy(app)
    Migrate(app, db) # attach for Alembic
    
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    
    return manager


if __name__ == '__main__':
    app     = create_app()
    manager = create_manager(app)
    
    manager.run()
