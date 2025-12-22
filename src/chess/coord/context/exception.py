# src/coord/exception.py

"""
Module: chess.coord.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.coord import CoordException
from chess.system import ContextException

__all__ = [
    # ======================# COORD_CONTEXT EXCEPTION #======================#
    "CoordContextException",
]


# ======================# COORD_CONTEXT EXCEPTION #======================#
class CoordContextException(CoordException, ContextException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by CoordContext objects.
    2.  Catchall for conditions which are not covered by lower level CoordContext exceptions.

    # PARENT:
        *   CoordException
        *   ContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_CONTEXT_ERROR"
    DEFAULT_ERROR_CODE = "CoordContext raised an exception."