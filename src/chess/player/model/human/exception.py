# src/chess/owner/model/human/exception.py

"""
Module: chess.owner.model.human.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.player import PlayerException

__all__ = [
    #======================# HUMAN_PLAYER EXCEPTION #======================#
    "HumanPlayerException",
]

#======================# HUMAN_PLAYER EXCEPTION #======================#
class HumanPlayerException(PlayerException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate an attribute, method, or operation organic to a HumanPlayer encountered a condition which
        caused a failure.
    2.  Wraps an exception that hits the try-finally block of an Player method.

    # PARENT:
        *   PlayerException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "HUMAN_PLAYER_ERROR"
    DEFAULT_MESSAGE = "HumanPlayer raised an exception."
    