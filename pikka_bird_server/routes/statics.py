from flask import Blueprint, jsonify

import pikka_bird_server


statics = Blueprint('statics', __name__)


@statics.route('/')
def index():
    """
        GET /
        Route of apex.
        """
    
    return jsonify({
        'service': 'pikka-bird-server',
        'version': pikka_bird_server.__version__})
