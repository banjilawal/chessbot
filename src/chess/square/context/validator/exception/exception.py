# src/chess/square/context/validator/exception/exception.py

"""
Module: chess.square.context.validator.exception.exception
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import ValidationException
from chess.square import SquareContextException



#========================= SQUARE_CONTEXT VALIDATION EXCEPTIONS =========================#
class InvalidSquareContextException(
    SquareContextException,
    ValidationException
):
    """Catchall Exception for SquareContextValidator when a candidate fails a sanity check.""""""
    ERROR_CODE = "SQUARE_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "SquareContext validation failed."