# src/chess/coord/context/validator/exception/null/exception.py

"""
Module: chess.coord.context.validator.exception.null.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.system import NullException
from chess.coord import InvalidCoordContextException


__all__ = [
    "NullCoordContextException"
]

# ========================= NULL COORD_SEARCH_CONTEXT EXCEPTIONS =========================#
class NullCoordContextException(InvalidCoordContextException, NullException):
    """Raised if an entity, method, or operation requires CoordContext but gets null instead."""
    ERROR_CODE = "NULL_COORD_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "CoordContext cannot be null."
