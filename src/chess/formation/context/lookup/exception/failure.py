# src/chess/formation/lookup/exception/failure.py

"""
Module: chess.formation.lookup.exception.failure
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.formation import InvalidBattleOrderException
from chess.system import LookupFailedException

__all__ = [
    # ======================# ORDER LOOKUP FAILED EXCEPTION #======================#
    "OrderLookupFailedException",
]


# ======================# ORDER LOOKUP FAILED EXCEPTION #======================#
class OrderLookupFailedException(InvalidBattleOrderException, LookupFailedException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an error occurred because a lookup is outside the range of acceptable BattleOrder lookups.

    # PARENT:
        *   InvalidBattleOrderException
        *   LookupFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ORDER_LOOKUP_FAILED_ERROR"
    DEFAULT_MESSAGE = "ForwardLookup failed failed because there is no configuration property includes that value."

