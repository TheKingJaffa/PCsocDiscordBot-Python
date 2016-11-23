from pony.orm import Database, db_session

DB_FILE = 'test.sqlite3'

db = Database()
db.bind('sqlite', DB_FILE, create_db=True)

class DictionaryMixin(object):
    @classmethod
    @db_session
    def create_or_update(cls, **kwargs):
        old_obj = cls.get(**dict((k, kwargs[k]) for k in cls._pk_columns_))
        if old_obj is None:
            return cls(**kwargs)
        for k, v in kwargs.items():
            if k not in cls._pk_columns_:
                setattr(old_obj, k, v)
        return old_obj
