

from itertools import count
from threading import Lock
from typing import Any, Type, TypeVar

T = TypeVar("T")


class AutoId:
    """
    # ROLE: Decorator

    # RESPONSIBILITY:
    1. Generate and issue unique, read-only thread safe IDs per class.
    2. Create counter starting at 1 for any class it decorates.

    # ATTRIBUTES:
    None
    """

    def __init__(self, start: int = 1, add_hash_eq: bool = True) -> object:
        """"""
        self.start = start
        self.add_hash_eq = add_hash_eq

    def __call__(self, cls: Type[T]) -> Type[T]:
        # Set up the counter and locking
        cls.id_counter = count(self.start)
        cls.id_lock = Lock()

        # The original init from the AutoId client class.
        original_init = cls.__init__

        # The generic type hints to satisfy static type checkers
        def new_init(self: Any, *args: Any, **kwargs:Any) -> None:

            # Generate the visitor_id when it has a lock.
            with cls.id_lock:
                self._visitor_id = next(cls.id_counter)

            # Call the original __init__ with all its args
            original_init(self, *args, **kwargs)

        def get_id(self):
            return self._visitor_id

        def repr_func(obj):
            return f"<{cls.__name__} visitor_id={obj.visitor_id}>"

        cls.__init__ = new_init
        cls.id = property(get_id)
        cls.__repr__ = repr_func

        return cls
        # cls.visitor_id = property(lambda self: self._visitor_id)

        # if self.add_hash_eq:
        #     if not hasattr(cls, "__eq__"):
        #         def __eq__(self, other: object) -> bool:
        #             if other is self:
        #                 return True
        #             if not isinstance(other, cls):
        #                 return NotImplemented
        #             return self._visitor_id == other
        #         cls.__eq__ = __eq__
        #
        #     if not hasattr(cls, "__hash__"):
        #         cls.__hash__ = lambda self: hash(self._visitor_id)
        #
        #     if not hasattr(cls, "__repr__"):
        #         cls.__repr__ = lambda self: f"<{cls.__name__}: visitor_id={self._visitor_id}>"
        #
        #     return cls
