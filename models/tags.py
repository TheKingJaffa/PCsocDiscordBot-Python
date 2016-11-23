from pony.orm import Required, PrimaryKey

from models.database import DictionaryMixin, Table, db


class Tag(db.Entity, Table, DictionaryMixin):
    user = Required(int, size=64)
    platform = Required(str)
    PrimaryKey(user, platform)
    tag = Required(str)
