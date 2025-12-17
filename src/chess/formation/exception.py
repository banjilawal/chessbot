# src/chess/formation/exception.py

"""
Module: chess.formation.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    "BattleOrderException",
]


class BattleOrderException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
    
    # RESPONSIBILITIES:
    1.  Super class af exceptions by BattleOrder objects.
    2.  Parent class of BattleOrder build/validation exceptions.

    # PARENT:
        *   ChessException
    
    # PROVIDES:
    None
    
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BATTLE_ORDER_ERROR"
    DEFAULT_MESSAGE = "BattleOrder raised an exception."
