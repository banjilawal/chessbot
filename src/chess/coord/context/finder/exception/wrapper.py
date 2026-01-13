# src/chess/coord/context/finder/exception/wrapper.py

"""
Module: chess.coord.context.finder.exception.wrapper
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""


from chess.coord import CoordException
from chess.system import SearchFailedException

__all__ = [
    # ======================# COORD_FINDER EXCEPTION #======================#
    "CoordSearchFailedException",
]


# ======================# COORD_FINDER EXCEPTION #======================#
class CoordSearchFailedException(CoordException, SearchFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised when CoordFinder objects.
    2.  Wraps an exception that hits the try-finally block of an CoordFinder method.

    # PARENT:
        *   CoordException
        *   FinderException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_FINDER_ERROR"
    DEFAULT_MESSAGE = "CoordFinder raised an exception."
