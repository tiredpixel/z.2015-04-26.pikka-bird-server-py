import datetime
from flask import json

from pikka_bird_server.models.collection import Collection
from pikka_bird_server.models.machine import Machine
from pikka_bird_server.models.report import Report
from pikka_bird_server.models.service import Service


class TestCollections:
    
    def test_create(self, client, collection_valid):
        res = client.post('/collections',
            data=json.dumps(collection_valid),
            headers={
                'Content-Type': 'application/json'},
            environ_base={
                'REMOTE_ADDR': '127.0.0.1'})
        data = json.loads(res.data)
        
        assert res.status_code == 201
        assert data == {}
        
        assert Machine.query.count() == 1
        machine = Machine.query.first()
        assert isinstance(machine.created_at, datetime.datetime)
        assert isinstance(machine.updated_at, datetime.datetime)
        assert machine.address == '127.0.0.1'
        assert machine.hostname is None
        
        assert Service.query.count() == 1
        service = Service.query.first()
        assert isinstance(service.created_at, datetime.datetime)
        assert service.code == 'system'
        
        assert Collection.query.count() == 1
        collection = Collection.query.first()
        assert isinstance(collection.created_at, datetime.datetime)
        assert collection.collected_at == datetime.datetime(2015, 4, 4, 19, 32, 20, 616977)
        assert collection.collecting_at == datetime.datetime(2015, 4, 4, 19, 33, 1, 424242)
        assert collection.hostname == 'localhost'
        assert collection.machine == machine
        assert collection.pid == 42
        
        assert Report.query.count() == 1
        report = Report.query.first()
        assert report.collection == collection
        assert report.data == {'load': {'avg_15_min': 1.62939453125}}
        assert report.service == service
    
    def test_create_no_content_type(self, client, collection_valid):
        res = client.post('/collections',
            data=json.dumps(collection_valid))
        data = json.loads(res.data)
        
        assert res.status_code == 415
        assert data == {}
        
        assert Machine.query.count() == 0
        assert Service.query.count() == 0
        assert Collection.query.count() == 0
        assert Report.query.count() == 0
