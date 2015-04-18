import pytest

from pikka_bird_server.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    
    return app.test_client()

@pytest.fixture
def collection_valid():
    return {
        'collected_at': '2015-04-04T19:32:20.616977',
        'collecting_at': '2015-04-04T19:33:01.424242',
        'hostname': 'localhost',
        'pid': 42,
        'reports': {
            'system': {
                'load': {
                    'avg_15_min': 1.62939453125}}}}
