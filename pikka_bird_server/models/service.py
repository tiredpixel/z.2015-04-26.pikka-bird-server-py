import pikka_bird_server.database as db
from pikka_bird_server.models.base import Base


class Service(db.Base, Base):
    """
        Service, such as `system`, `postgresql`, `mysql`.
        """
    
    __table__ = db.Base.metadata.tables['services']
    
    def __init__(self, code):
        self.code = code
    
    def __repr__(self):
        return '<Service %r>' % self.code
