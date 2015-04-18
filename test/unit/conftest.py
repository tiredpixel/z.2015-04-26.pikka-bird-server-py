import os
if os.environ.get('CI') != '1':
    exit("!!! CI environment variable must be set for testing environment")


import pytest

import pikka_bird_server.database as db

@pytest.fixture(autouse=True)
def db_implode():
    tables = [
        'collections',
        'machines',
        'reports',
        'services']
    
    sql = 'TRUNCATE ' + ', '.join(tables)
    
    db.db_session.execute(sql)
