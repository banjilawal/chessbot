# src/chess/formation/validator/exception/flag.py

"""
Module: chess.formation.validator.exception.flag
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import BoundsException
from chess.formation import InvalidOrderContextException

__all__ = [
    # ========================= NO_ORDER_CONTEXT_FLAG EXCEPTION =========================#
    "ZeroOrderContextFlagsException",
    # ========================= TOO_MANY_ORDER_CONTEXT_FLAGS EXCEPTION =========================#
    "ExcessiveOrderContextFlagsException"
]


# ========================= ZERO_ORDER_CONTEXT_FLAFS EXCEPTION =========================#
class ZeroOrderContextFlagsException(InvalidOrderContextException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate no OrderContext flag is provided for a Formation lookup.

    # PARENT:
        *   BoundsException
        *   InvalidOrderContextException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_ORDER_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "No OrderContext flag was selected. A map flag must be turned on with a target value."
