import socket

import pikka_bird_server.database as db
from pikka_bird_server.models.base import Base


class Machine(db.Base, Base):
    """
        Machine for which metrics are collected. Machines are referenced
        uniquely by IP, not hostname. If a server changes IP, it is considered a
        new Machine. Servers running collectors must send directly, and not
        through a NAT. If multiple networks need to be joined, it is probably
        easiest to run a server within each, but writing to the same database.
        
        Hostnames are stored in two places: as reported by the collector within
        a Collection (db `collections.hostname`); and, if verified, within a
        Machine (db `machines.hostname`). It is expected that all hostnames are
        resolvable by the server. If they are not, things should still work, but
        only IP will be available. This is intended to be a level of protection
        against collectors reporting misconfigured hostnames.
        """
    
    __table__ = db.Base.metadata.tables['machines']
    
    def __init__(self, address):
        self.address = address
    
    def __repr__(self):
        return '<Machine %r>' % self.address
    
    def update_hostname(self, hostname):
        """
            Update hostname, if it can be resolved.
            
            PARAMETERS:
                hostname : string
                    hostname to resolve and set
            
            RETURN:
                : boolean, None
                    None:  hostname not changed
                    True:  hostname resolved and updated
                    False: hostname not resolved
            """
        
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
