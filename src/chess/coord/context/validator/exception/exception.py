# src/chess/coord/context/validator/exception/exception.py

"""
Module: chess.coord.context.validator.exception.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""



from chess.system import ValidationException
from chess.coord import CoordContextException


__all__ = [
    "InvalidCoordContextException"
]


#========================= COORD_CONTEXT VALIDATION EXCEPTIONS =========================#
class InvalidCoordContextException(CoordContextException, ValidationException):
    """Catchall Exception for CoordContextValidator when a candidate fails a sanity check."""
    ERROR_CODE = "COORD_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "CoordContext validation failed."