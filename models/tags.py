from pony.orm import Required, PrimaryKey

from models.database import db, DictionaryMixin


class Tag(db.Entity, DictionaryMixin):
    user = Required(int, size=64)
    platform = Required(str)
    PrimaryKey(user, platform)
    tag = Required(str)
