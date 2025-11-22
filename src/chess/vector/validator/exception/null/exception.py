# src/chess/vector/validator/exception/null/exception.py

"""
Module: chess.vector.validator.exception.null.exception_
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system import NullException
from chess.vector import InvalidVectorException



__all__ = [
    "NullInvalidVectorException",
    "NullXComponentException",
    "NullYComponentException",
]

# ======================# NULL VECTOR EXCEPTION #======================#
class NullInvalidVectorException(InvalidVectorException, NullException):
    """Raised if an entity, method, or operation requires Vector but gets validation instead."""
    ERROR_CODE = "NULL_VECTOR_ERROR"
    DEFAULT_MESSAGE = "Vector cannot be validation."


# ======================# NULL COMPONENT EXCEPTIONS #======================#  
class NullXComponentException(InvalidVectorException, NullException):
    """Raised if Vector's x dimension is validation."""
    ERROR_CODE = "VECTOR_NULL_X_DIMENSION_ERROR"
    DEFAULT_MESSAGE = "Vector's X-dimension cannot be validation."


class NullYComponentException(InvalidVectorException, NullException):
    """Raised if a Vector's y dimension is validation."""
    ERROR_CODE = "VECTOR_NULL_Y_DIMENSION_ERROR"
    DEFAULT_MESSAGE = "Vector's Y-dimension cannot be validation."