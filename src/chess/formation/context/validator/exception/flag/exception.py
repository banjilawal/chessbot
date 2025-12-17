# src/chess/formation/context/validator/exception/flag/exception.py

"""
Module: chess.formation.context.validator.exception.flag.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.formation import InvalidBattleOrderContextException

__all__ = [
    # ========================= NO_BATTLE_ORDER_CONTEXT_FLAG EXCEPTION =========================#
    "NoBattleOrderContextFlagException",
    # ========================= TOO_MANY_BATTLE_ORDER_CONTEXT_FLAGS EXCEPTION =========================#
    "TooManyBattleOrderContextFlagsException"
]


# ========================= NO_BATTLE_ORDER_CONTEXT_FLAG EXCEPTION =========================#
class NoBattleOrderContextFlagException(InvalidBattleOrderContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate no BattleOrderContext flag is provided with a searcher value.

    # PARENT:
        *   InvalidBattleOrderContextException
        *   ContextFlagCountException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_BATTLE_ORDER_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "No BattleOrderContext flag was selected. A context flag must be turned on with a target value."


# ========================= TOO_MANY_BATTLE_ORDER_CONTEXT_FLAGS EXCEPTION =========================#
class TooManyBattleOrderContextFlagsException(InvalidBattleOrderContextException, ContextFlagCountException):
    """
    # ROLE: ContextFlagException, BattleOrderContextException

    # RESPONSIBILITIES:
    1.  Indicate if more than one BattleOrder attribute is going to be used in an BattleOrderFinder.

    # PARENT:
        *   InvalidBattleOrderContextException
        *   ContextFlagCountException

    # PROVIDES:
        *   TooManyBattleOrderContextFlagsException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOO_MANY_BATTLE_ORDER_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "More than one BattleOrderContext flag was selected. Only one context flag is allowed."