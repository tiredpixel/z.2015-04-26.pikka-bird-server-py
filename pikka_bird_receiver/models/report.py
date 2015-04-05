from sqlalchemy import orm

from pikka_bird_receiver.database import Base


class Report(Base):
    __table__ = Base.metadata.tables['reports']
    
    collection = orm.relationship('Collection',
        backref=orm.backref('reports'))
    
    service = orm.relationship('Service',
        backref=orm.backref('reports'))
    
    def __repr__(self):
      return '<Report %r>' % self.id
