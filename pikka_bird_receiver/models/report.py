from sqlalchemy import orm

import pikka_bird_receiver.database as db
from pikka_bird_receiver.models.base import Base


class Report(db.Base, Base):
    __table__ = db.Base.metadata.tables['reports']
    
    collection = orm.relationship('Collection',
        backref=orm.backref('reports'))
    
    service = orm.relationship('Service',
        backref=orm.backref('reports'))
    
    def __repr__(self):
      return '<Report %r>' % self.id
