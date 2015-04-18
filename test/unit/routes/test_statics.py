from flask import json

import pikka_bird_server


class TestStatics:
    
    def test_index(self, client):
        res  = client.get('/')
        data = json.loads(res.data)
        
        assert res.status_code == 200
        assert data == {
            'service': 'pikka-bird-server',
            'version': pikka_bird_server.__version__}
