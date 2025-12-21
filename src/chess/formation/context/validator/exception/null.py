# src/chess/formation/map/validator/exception/null.py

"""
Module: chess.formation.map.validator.exception.null
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import NullException
from chess.formation import InvalidOrderContextException

__all__ = [
    # ======================# ORDER_CONTEXT NULL EXCEPTION #======================#
    "NullOrderContextException",
]


# ======================# ORDER_CONTEXT NULL EXCEPTION #======================#
class NullOrderContextException(InvalidOrderContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an OrderContext validation candidate is null.
    2.  Raised if an entity, method or operation requires an OrderContext but receives null instead.

    # PARENT:
        *   InvalidOrderContextException
        *   NullException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_ORDER_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "OrderContext cannot be null."