# src/chess/coord/context/validator/exception/debug/null

"""
Module: chess.coord.context.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_COORD_CONTEXT EXCEPTION #======================#
    "NullCoordContextException",
]

from chess.system import NullException
from chess.coord import InvalidCoordContextException

# ======================# NULL_COORD_CONTEXT EXCEPTION #======================#
class NullCoordContextException(InvalidCoordContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that CoordContext validation failed because the candidate was null.

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
    ERROR_CODE = "NULL_COORD_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "CoordContext validation failed: The candidate was null."