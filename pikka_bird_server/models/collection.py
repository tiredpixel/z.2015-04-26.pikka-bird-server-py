from sqlalchemy import orm

import pikka_bird_server.database as db
from pikka_bird_server.models.base import Base


class Collection(db.Base, Base):
    __table__ = db.Base.metadata.tables['collections']
    
    machine = orm.relationship('Machine',
        backref=orm.backref('collections'))
    
    def __repr__(self):
        return '<Collection %r>' % self.id
