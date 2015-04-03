#!/usr/bin/env python

import os
from flask import Flask, jsonify

import pikka_bird_receiver.routes.statics


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    
    app.register_blueprint(pikka_bird_receiver.routes.statics.statics)
    
    return app


if __name__ == "__main__":
    debug = (int(os.environ['DEBUG']) == 1)
    
    app = create_app(debug=debug)
    app.run()
