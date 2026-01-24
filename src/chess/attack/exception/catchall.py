# src/chess/attack/exception/catchall.py

"""
Module: chess.attack.exception.catchall
Author: Banji Lawal
Created: 2025-01-24
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# ATTACK EXCEPTION #======================#
    "AttackException",
]


# ======================# ATTACK EXCEPTION #======================#
class AttackException(ChessException):
    """
    # ROLE: Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Catchall for Attack and parent of exceptions raised by things Attack is responsible for.
  
    # PARENT:
        *   ChessException
  
    # PROVIDES:
    None
  
    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "ATTACK_ERROR"
    DEFAULT_MESSAGE = "Attack raised an exception."