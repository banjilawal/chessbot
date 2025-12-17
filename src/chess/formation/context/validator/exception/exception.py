# src/chess/formation/context/validator/exception/exception.py

"""
Module: chess.formation.context.validator.exception.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.formation import BattleOrderContextException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# TEAM_SCHEMA_CONTEXT VALIDATION SUPER CLASS #======================#
    "InvalidBattleOrderContextException",
]




# ======================# TEAM_SCHEMA_CONTEXT VALIDATION SUPER CLASS #======================#
class InvalidBattleOrderContextException(BattleOrderContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised BattleOrderContext validation.
    2.  Wraps unhandled exceptions that hit the finally-block in BattleOrderContextValidator methods.

    # PARENT:
        *   BattleOrderContextException
        *   ValidationFailedException

    # PROVIDES:
        *   InvalidBattleOrderContextException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_SCHEMA_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "BattleOrderContext validation failed."