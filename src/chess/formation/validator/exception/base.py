# src/chess/formation/validator/exception/base.py

"""
Module: chess.formation.validator.exception.base
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


from chess.formation import BattleOrderException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# BATTLEORDER VALIDATION EXCEPTION #======================#
    "InvalidBattleOrderException",
]


# ======================# BATTLE_ORDER VALIDATION EXCEPTION #======================#
class InvalidBattleOrderException(BattleOrderException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during an BattleOrder verification process.
    2.  Catchall Exception for BattleOrderValidator when a candidate fails a sanity check.
    3.  Wraps unhandled exceptions that hit the try-finally block of an BattleOrderValidator method.

    # PARENT:
        *   BattleOrderException
        *   ValidationFailedException

    # PROVIDES:
    InvalidBattleOrderException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "BATTLEORDER_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "BattleOrder validation failed."