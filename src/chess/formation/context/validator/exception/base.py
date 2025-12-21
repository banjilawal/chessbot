# src/chess/formation/map/validator/exception/base.py

"""
Module: chess.formation.map.validator.exception.base
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.formation import OrderContextException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# ORDER_CONTEXT VALIDATION EXCEPTION #======================#
    "InvalidOrderContextException",
]




# ======================# ORDER_CONTEXT VALIDATION EXCEPTION #======================#
class InvalidOrderContextException(OrderContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised OrderContext validation.
    2.  Wraps unhandled exceptions that hit the finally-block in OrderContextValidator methods.

    # PARENT:
        *   OrderContextException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ORDER_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "OrderContext validation failed."