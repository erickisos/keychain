from typing import List
from ..protocols.db import IDb
from ..adapters import key as a_key


def find(user_id, db: IDb) -> List:
    return db.find(user_id, db)


def create(user_id, item, db: IDb):
    return db.insert(user_id, item, db)
