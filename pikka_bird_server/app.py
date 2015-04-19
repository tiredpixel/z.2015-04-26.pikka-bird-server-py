import logging
import os
import sys

from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException, default_exceptions

import pikka_bird_server.database
import pikka_bird_server.routes.collections
import pikka_bird_server.routes.statics


def create_app():
    """
        Create application, using Flask. Payloads are in JSON.
        """
    
    app = Flask('pikka_bird_server')
    
    app.debug = (os.environ['LOG_LEVEL'] == 'DEBUG')
    
    for r in [
        'collections',
        'statics']:
        app.register_blueprint(
            getattr(getattr(pikka_bird_server.routes, r), r))
    
    for code in default_exceptions.keys():
        app.error_handler_spec[None][code] = __make_json_error
    
    __setup_logger(app.logger)
    
    return app

# http://flask.pocoo.org/snippets/83/
# thanks, Pavel Repin
def __make_json_error(ex):
    response = jsonify(message=str(ex))
    response.status_code = (ex.code
                            if isinstance(ex, HTTPException)
                            else 500)
    return response

def __setup_logger(logger):
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s -- %(name)s: %(message)s')
    
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    
    logger.setLevel(os.environ['LOG_LEVEL'])
    logger.addHandler(handler)
