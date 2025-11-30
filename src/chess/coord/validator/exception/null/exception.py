# src/chess/coord/validator/exception/null/exception.py

"""
Module: chess.coord.validator.exception.null.exception
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import NullException
from chess.coord import InvalidCoordException

__all__ = [
    "NullCoordException",
    "NullRowException",
    "NullColumnException",
]

# ====================== NULL COORD EXCEPTIONS #======================#
class NullCoordException(InvalidCoordException, NullException):
    """Raised if an entity, method, or operation requires Coord but gets null instead."""
    ERROR_CODE = "NULL_COORD_ERROR"
    DEFAULT_MESSAGE = "Coord cannot be validation"

# ====================== NULL COORD_ROW VALIDATION EXCEPTIONS #======================#
class NullRowException(InvalidCoordException, NullException):
    """Raised if Coord.row is validation."""
    ERROR_CODE = "NULL_COORD_ROW_ERROR"
    DEFAULT_MESSAGE = "Coord.row property cannot be null."


# ====================== NULL COORD_COLUMN VALIDATION EXCEPTIONS #======================#
class NullColumnException(InvalidCoordException, NullException):
    """Raised if Coord.row is validation."""
    ERROR_CODE = "NULL_COORD_COLUMN_INDEX_ERROR"
    DEFAULT_MESSAGE = "Coord.column property cannot be null."