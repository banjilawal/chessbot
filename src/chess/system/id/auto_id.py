# src/chess/system/id/auto_id.py

"""
Module: chess.system.id.auto_id
Author: Banji Lawal
Created: 2025-10-09
Updated: 2025-10-10

# SECTION 1 - Purpose:
1. This module provides a satisfaction of the `ChessBot` consistency requirement. The satisfaction covers
    enforcement of regulations for unique IDs in the system.

# SECTION 2 - Scope:
The module only covers the generating and publishing IDs.

# SECTION 3 - Limitations:
  1. This module is not responsible for verifying the uniqueness of an ID. the `AutoId` class in
      `chess.system.id.auto_id` module.

# SECTION 4 - Design Considerations and Themes:
Major themes influencing the design include:
1. Speed
2. Uniqueness.
3. Scalability


# SECTION 5 - Features Supporting Requirements:
1. No direct support for any user level features.
2. Direct support for consistency.
3. Cutting down on boilerplate manually generating a unique ID emitter for each class.
4. Providing identification to entities that did not originally have that.

# SECTION G - Feature Delivery Mechanism:
1. Writing a class that has the same functionality as `AtomicLong` in `Java`.
2. Making the class a decorator to leave existing code in the class alone.

# SECTION 7 - Dependencies:
* From Python `itertools` library:
    `count`

* From Python `threading` Library:
    `Lock`

* From Python `typing` Library:
    `Type`, `TypeVar`

# SECTION 8 - Contains:
1. `AutoId
"""

from itertools import count
from threading import Lock
from typing import Type, TypeVar

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

    def __init__(self, start: int=1, add_hash_eq: bool=True):
        """

        """
        self.start = start
        self.add_hash_eq = add_hash_eq

    def __call__(self, cls: Type[T]) -> Type[T]:
        """
        Decorate the given class with automatic ID assignment.
        """
        cls.id_counter = count(self.start)
        cls.id_lock = Lock()

        original_init = cls.__init__

        def new_init(self, *args, **kwargs):
            with cls.id_lock:
                self._id = next(cls.id_counter)
            original_init(self, *args, **kwargs)

        def get_id(self):
            return self._id

        def repr_func(obj):
            return f"<{cls.__name__} id={obj.id}>"

        cls.__init__ = new_init
        cls.id = property(get_id)
        cls.__repr__ = repr_func

        return cls
        # cls.id = property(lambda self: self._id)

        # if self.add_hash_eq:
        #     if not hasattr(cls, "__eq__"):
        #         def __eq__(self, other: object) -> bool:
        #             if other is self:
        #                 return True
        #             if not isinstance(other, cls):
        #                 return NotImplemented
        #             return self._id == other
        #         cls.__eq__ = __eq__
        #
        #     if not hasattr(cls, "__hash__"):
        #         cls.__hash__ = lambda self: hash(self._id)
        #
        #     if not hasattr(cls, "__repr__"):
        #         cls.__repr__ = lambda self: f"<{cls.__name__}: id={self._id}>"
        #
        #     return cls
