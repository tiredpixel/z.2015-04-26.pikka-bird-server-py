from sqlalchemy import orm

import pikka_bird_receiver.database as db
from pikka_bird_receiver.models.base import Base


class Collection(db.Base, Base):
    __table__ = db.Base.metadata.tables['collections']
    
    machine = orm.relationship('Machine',
        backref=orm.backref('collections'))
    
    def __repr__(self):
        return '<Collection %r>' % self.id
