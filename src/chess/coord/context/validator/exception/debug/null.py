# src/chess/coord/validator/exception/null/exception.py

"""
Module: chess.coord.validator.exception.null.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.system import NullException
from chess.coord import InvalidCoordContextException

__all__ = [
    # ======================# NULL_COORD_CONTEXT EXCEPTION #======================#
    "NullCoordContextException",
]


# ======================# NULL_COORD_CONTEXT EXCEPTION #======================#
class NullCoordContextException(InvalidCoordContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if a CoordContext validation candidate is null.
    2.  Raised if an entity, method or operation requires a CoordContext but receives null instead.

    # PARENT:
        *   NullCoordContextException
        *   InvalidCoordContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_COORD_CONTEXT__ERROR"
    DEFAULT_MESSAGE = "CoordContext cannot be null."