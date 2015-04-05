from sqlalchemy.exc import IntegrityError


class Base:
    __cache_find = {}
    
    @classmethod
    def find(cls, cached=False, **kwargs):
        if cached:
            cache_key = tuple(kwargs.items())
            
            r = cls.__cache_find.get(cache_key)
        else:
            r = cls.query.filter_by(**kwargs).first()
        
        if r is None:
            r = cls(**kwargs)
            cls.query.session.add(r)
            
            try:
                cls.query.session.commit()
            except IntegrityError:
                cls.query.session.rollback()
                r = cls.query.filter_by(**kwargs).first()
            
            if cached:
                cls.__cache_find[cache_key] = r
        
        return r
