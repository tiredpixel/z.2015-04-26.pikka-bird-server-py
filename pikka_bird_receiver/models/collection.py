from sqlalchemy import orm

from pikka_bird_receiver.database import Base


class Collection(Base):
    __table__ = Base.metadata.tables['collections']
    
    machine = orm.relationship('Machine',
        backref=orm.backref('collections'))
    
    def __repr__(self):
        return '<Collection %r>' % self.id
