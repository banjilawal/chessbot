# src/chess/vector/builder.py
"""
Module: chess.vector.builder
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0

# SCOPE:
-------
**Limitation**: There is no guarantee properly created `Vector` objects released by the module will satisfy client
    requirements. Clients are responsible for ensuring a `VectorBuilder` product will not fail when used. Products
    from `VectorBuilder` --should-- satisfy `VectorValidator` requirements.

**Related Features**:
    Authenticating existing vectors -> See VectorValidator, module[chess.vector.validator],
    Handling process and rolling back failures --> See `Transaction`, module[chess.system]

# THEME:
-------
* Data assurance, error prevention

**Design Concepts**:
    Separating object creation from object usage.
    Keeping constructors lightweight

# PURPOSE:
---------
1. Central, single producer of authenticated `Vector` objects.
2. Putting all the steps and logging into one place makes modules using `Vector` objects cleaner and easier to follow.

**Satisfies**: Reliability and performance contracts.

# DEPENDENCIES:
---------------
From `chess.system`:
    `BuildResult`, `Builder`, `KNIGHT_STEP_SIZE`, `LoggingLevelRouter`, `ChessException`, `NullException`
    `BuildFailedException`

From `chess.vector`:
    `Vector`, `NullVectorException`, `VectorBuildFailedException`, `NullXComponentException`,
    `NullYComponentException`, `VectorBelowBoundsException`, `VectorAboveBoundsException`

# CONTAINS:
----------
 * `VectorBuilder`
"""
from itertools import count
from threading import Lock
from typing import Type, TypeVar, Callable

T = TypeVar("T")


class AutoId:
    """
    # ROLE: Decorator
    ------


    # RESPONSIBILITY:
    ----------------
    1. Generate and issue unique, read-only thread safe IDs per class.
    2. Create counter starting at 1 for any class it decorates.

    # ATTRIBUTES:
    ------------
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
