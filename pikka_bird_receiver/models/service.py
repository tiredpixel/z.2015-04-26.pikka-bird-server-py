import pikka_bird_receiver.database as db
from pikka_bird_receiver.models.base import Base


class Service(db.Base, Base):
    __table__ = db.Base.metadata.tables['services']
    
    def __init__(self, code):
        self.code = code
    
    def __repr__(self):
        return '<Service %r>' % self.code
