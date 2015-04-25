import os
if os.environ.get('CI') != 'true':
    exit("!!! CI environment variable must be set for testing environment")


import pytest

import pikka_bird_server.database as db
from pikka_bird_server.models.service import Service

@pytest.fixture(autouse=True)
def db_implode():
    tables = [
        'collections',
        'machines',
        'reports',
        'services']
    
    sql = 'TRUNCATE ' + ', '.join(tables)
    
    db.db_session.execute(sql)
    
    Service._Base__cache_find = {}
