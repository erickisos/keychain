from abc import ABC
from typing import List, Protocol, TypeVar

T = TypeVar('T')


class IDb(Protocol[T]):
    def fetch(self, user_id, item_id, db) -> T:
        ...

    def find(self, user_id, db) -> List[T]:
        ...

    def insert(self, user_id, item, db) -> T:
        ...

    def upsert(self, user_id, item, db) -> T:
        ...

    def retract(self, user_id, item_id, db) -> T:
        ...
