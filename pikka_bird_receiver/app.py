import logging
import os
import sys

from flask import Flask

import pikka_bird_receiver.database
import pikka_bird_receiver.routes.collections
import pikka_bird_receiver.routes.statics


def create_app():
    app = Flask('pikka_bird_receiver')
    
    app.debug = (os.environ['LOG_LEVEL'] == 'DEBUG')
    
    for r in [
        'collections',
        'statics']:
        app.register_blueprint(
            getattr(getattr(pikka_bird_receiver.routes, r), r))
    
    __setup_logger(app.logger)
    
    return app

def __setup_logger(logger):
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s -- %(name)s: %(message)s')
    
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    
    logger.setLevel(os.environ['LOG_LEVEL'])
    logger.addHandler(handler)
