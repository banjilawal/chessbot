# src/chess/formation/lookup/exception/base.py

"""
Module: chess.formation.lookup.exception.base
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ServiceException
from chess.formation import BattleOrderException


__all__ = [
    # ======================# TEAM_SCHEMA_LOOKUP EXCEPTION #======================#
    "BattleOrderLookupException",
]


# ======================# TEAM_SCHEMA_LOOKUP EXCEPTION #======================#
class BattleOrderLookupException(BattleOrderException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by BattleOrderLookup objects.
    2.  Raised when no specific exception exists for the error interrupting BattleOrderLookup's
        processes from their normal flows.

    # PARENT:
        *   BattleOrderException
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_LOOKUP_ERROR"
    DEFAULT_MESSAGE = "TeamLookup raised an exception."