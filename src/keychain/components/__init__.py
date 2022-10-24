from typing import Any, Dict


class Singleton(type):
    __instances: Dict[Any, Any] = {}

    def __call__(self, *args, **kwargs):
        if self not in self.__instances:
            self.__instances[self] = super(Singleton, self).__call__(
                *args, **kwargs
            )
        return self.__instances[self]
