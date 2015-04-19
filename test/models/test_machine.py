from pikka_bird_server.models.machine import Machine


class TestMachine:
    
    def test_update_hostname(self):
        machine = Machine('127.0.0.1')
        
        assert machine.hostname is None
        
        s = machine.update_hostname('localhost')
        
        assert s == True
        assert machine.hostname == 'localhost'
    
    def test_update_hostname_same(self):
        machine = Machine('127.0.0.1')
        machine.hostname = 'localhost'
        
        assert machine.hostname == 'localhost'
        
        s = machine.update_hostname('localhost')
        
        assert s is None
        assert machine.hostname == 'localhost'
    
    def test_update_hostname_unresolvable(self):
        machine = Machine('127.0.0.1')
        
        assert machine.hostname is None
        
        s = machine.update_hostname('incredible-flying-mushroom')
        
        assert s == False
        assert machine.hostname is None
    
    def test_update_hostname_mismatch(self):
        machine = Machine('127.0.0.1')
        
        assert machine.hostname is None
        
        s = machine.update_hostname('example.com')
        
        assert s == False
        assert machine.hostname is None
