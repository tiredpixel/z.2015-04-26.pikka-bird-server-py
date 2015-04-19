import socket

import pikka_bird_server.database as db
from pikka_bird_server.models.base import Base


class Machine(db.Base, Base):
    __table__ = db.Base.metadata.tables['machines']
    
    def __init__(self, address):
        self.address = address
    
    def __repr__(self):
        return '<Machine %r>' % self.address
    
    def update_hostname(self, hostname):
        if self.hostname == hostname:
            return # skip
        
        try:
            hostname_address = socket.gethostbyname(hostname)
        except socket.gaierror:
            return False
        
        if self.address == hostname_address:
            self.hostname = hostname
            return True
        else:
            return False
