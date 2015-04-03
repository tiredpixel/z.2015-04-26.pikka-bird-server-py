#!/usr/bin/env python


import os

from pikka_bird_receiver.app import create_app


debug = (int(os.environ['DEBUG']) == 1)

app = create_app(debug=debug)

if __name__ == '__main__':
    app.run()
