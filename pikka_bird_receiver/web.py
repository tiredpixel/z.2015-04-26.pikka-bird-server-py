#!/usr/bin/env python


from pikka_bird_receiver.app import create_app


app = create_app()


if __name__ == '__main__':
    app.run()
