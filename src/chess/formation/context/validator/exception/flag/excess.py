# src/chess/formation/validator/exception/flag.py

"""
Module: chess.formation.validator.exception.flag
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.formation import InvalidOrderContextException

__all__ = [
    # ========================= NO_ORDER_CONTEXT_FLAG EXCEPTION =========================#
    # ========================= TOO_MANY_ORDER_CONTEXT_FLAGS EXCEPTION =========================#
    "ExcessiveOrderContextFlagsException"
]


# ========================= TOO_MANY_ORDER_CONTEXT_FLAGS EXCEPTION =========================#
class ExcessiveOrderContextFlagsException(InvalidOrderContextException, ContextFlagCountException):
    """
    # ROLE: ContextFlagException, OrderContextException

    # RESPONSIBILITIES:
    1.  Indicate if more than one TeamOrder attribute is going to be used in a Formation lookup.

    # PARENT:
        *   InvalidOrderContextException
        *   ContextFlagCountException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOO_MANY_ORDER_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "More than one OrderContext flag was selected. Only one map flag is allowed."