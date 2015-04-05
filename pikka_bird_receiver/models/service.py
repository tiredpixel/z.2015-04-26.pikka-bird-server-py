from pikka_bird_receiver.database import Base


class Service(Base):
    __table__ = Base.metadata.tables['services']
    
    def __init__(self, code):
        self.code = code
    
    def __repr__(self):
        return '<Service %r>' % self.code
