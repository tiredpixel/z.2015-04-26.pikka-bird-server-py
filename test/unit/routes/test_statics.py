from flask import json

import pikka_bird_receiver


class TestStatics:
    
    def test_index(self, client):
        res  = client.get('/')
        data = json.loads(res.data)
        
        assert res.status_code == 200
        assert data == {
            'service': 'pikka-bird-receiver',
            'version': pikka_bird_receiver.__version__}
