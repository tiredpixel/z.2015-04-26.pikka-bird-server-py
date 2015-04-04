import pytest

import pikka_bird_receiver.web


@pytest.fixture
def client():
    app = pikka_bird_receiver.web.create_app()
    app.testing = True
    
    return app.test_client()
