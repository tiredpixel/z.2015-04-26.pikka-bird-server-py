import pikka_bird_server.database as db
from pikka_bird_server.models.base import Base


class Machine(db.Base, Base):
    __table__ = db.Base.metadata.tables['machines']
    
    def __init__(self, address):
        self.address = address
    
    def __repr__(self):
        return '<Machine %r>' % self.address
