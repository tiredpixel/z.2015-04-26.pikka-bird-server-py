#!/usr/bin/env python

from flask import Flask, jsonify

import pikka_bird_receiver.routes.statics


app = Flask(__name__)

app.register_blueprint(pikka_bird_receiver.routes.statics.statics)


if __name__ == "__main__":
    app.run()
