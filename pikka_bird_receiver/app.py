from flask import Flask, jsonify

import pikka_bird_receiver.routes.statics


def create_app(debug=False):
    app = Flask('pikka_bird_receiver')
    app.debug = debug
    
    app.register_blueprint(pikka_bird_receiver.routes.statics.statics)
    
    return app
