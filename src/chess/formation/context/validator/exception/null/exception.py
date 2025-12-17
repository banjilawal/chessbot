# src/chess/formation/context/validator/exception/flag/__init__.py

"""
Module: chess.formation.context.validator.exception.flag.__init__
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import NullException
from chess.formation import InvalidBattleOrderContextException

__all__ = [
    # ======================# BATTLE_ORDER_CONTEXT NULL EXCEPTIONS #======================#
    "NullBattleOrderContextException",
]


# ======================# BATTLE_ORDER_CONTEXT NULL EXCEPTIONS #======================#
class NullBattleOrderContextException(InvalidBattleOrderContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an BattleOrderContext validation candidate is null.
    2.  Raised if an entity, method or operation requires an BattleOrderContext but receives null instead.

    # PARENT:
        *   InvalidBattleOrderContextException
        *   NullBattleOrderContextException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_BATTLE_ORDER_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "BattleOrderContext cannot be null."