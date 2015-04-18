import pikka_bird_receiver.database as db
from pikka_bird_receiver.models.base import Base


class Machine(db.Base, Base):
    __table__ = db.Base.metadata.tables['machines']
    
    def __init__(self, address):
        self.address = address
    
    def __repr__(self):
        return '<Machine %r>' % self.address
