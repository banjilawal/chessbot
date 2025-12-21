# src/chess/coord/map/validator/exception/exception.py

"""
Module: chess.coord.map.validator.exception.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.coord import CoordContextException
from chess.system import ValidationFailedException



__all__ = [
    # ========================= COORD_CONTEXT VALIDATION EXCEPTION =========================#
    "InvalidCoordContextException"
]


#========================= COORD_CONTEXT VALIDATION EXCEPTION =========================#
class InvalidCoordContextException(CoordContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised CoordContext validation.
    2.  Wraps unhandled exception that hit the finally-block in CoordContextValidator methods.

    # PARENT:
        *   CoordContextException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "CoordContext validation failed."