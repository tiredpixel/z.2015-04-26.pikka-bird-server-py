from pikka_bird_receiver.database import Base


class Machine(Base):
    __table__ = Base.metadata.tables['machines']
    
    def __init__(self, address):
        self.address = address
    
    def __repr__(self):
        return '<Machine %r>' % self.address
