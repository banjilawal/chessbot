# src/chess/formation/lookup/exception/base.py

"""
Module: chess.formation.lookup.exception.base
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


from chess.formation import FormationException


__all__ = [
    # ======================# BATTLE_ORDER_LOOKUP EXCEPTION #======================#
    "FormationLookupException",
]


# ======================# BATTLE_ORDER_LOOKUP EXCEPTION #======================#
class FormationLookupException(FormationException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by BattleOrderLookup objects.
    2.  Wrap an exception that hits the try-finally block of a BattleOrderLookup method.

    # PARENT:
        *   FormationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BATTLE_ORDER_LOOKUP_ERROR"
    DEFAULT_MESSAGE = "BattleOrderLookup raised an exception."