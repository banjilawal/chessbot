# src/chess/formation/context/exception.py

"""
Module: chess.formation.context.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ContextException


__all__ = [
    # ======================# BATTLE_ORDER_CONTEXT EXCEPTION #======================#
    "BattleOrderContextException",
]



# ======================# BATTLE_ORDER_CONTEXT EXCEPTION #======================#
class BattleOrderContextException(ContextException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by BattleOrderContext objects.
    2.  Catchall for conditions which are not covered by lower level BattleOrderContext exceptions.

    # PARENT:
        *   ContextException

    # PROVIDES:
    BattleOrderContextException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BATTLE_ORDER_CONTEXT_ERROR"
    DEFAULT_ERROR_CODE = "BattleOrderContext raised an exception."