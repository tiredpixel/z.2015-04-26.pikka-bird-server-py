from flask import Blueprint, jsonify

import pikka_bird_receiver


statics = Blueprint('statics', __name__)


@statics.route('/')
def index():
    return jsonify({
        'service': 'pikka-bird-receiver',
        'version': pikka_bird_receiver.__version__})
