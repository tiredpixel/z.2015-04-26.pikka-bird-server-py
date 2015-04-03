from flask import json
import pikka_bird_receiver
from pikka_bird_receiver.web import create_app


class TestStatics:
    
    def setup(self):
        app = create_app()
        app.testing = True
        self.app = app.test_client()
    
    def teardown(self):
        pass
    
    def test_statics_index(self):
        res  = self.app.get('/')
        data = json.loads(res.data)
        
        assert res.status_code == 200
        assert data == {
            'service': 'pikka-bird-receiver',
            'version': pikka_bird_receiver.__version__}
