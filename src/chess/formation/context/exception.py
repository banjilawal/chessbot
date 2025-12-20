# src/chess/formation/context/exception.py

"""
Module: chess.formation.context.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ContextException

__all__ = [
    # ======================# ORDER_CONTEXT EXCEPTION #======================#
    "OrderContextException",
]


# ======================# ORDER_CONTEXT EXCEPTION #======================#
class OrderContextException(ContextException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by OrderContext objects.
    2.  Catchall for conditions which are not covered by lower level OrderContext exceptions.

    # PARENT:
        *   ContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ORDER_CONTEXT_ERROR"
    DEFAULT_ERROR_CODE = "OrderContext raised an exception."