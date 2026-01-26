# src/chess/team/roster/exception/insertion/wrapper.py

"""
Module: chess.team.roster.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.square import SquareException
from chess.system import InsertionFailedException
from chess.team import TeamRosterException

__all__ = [
    # ======================# ADDING_SQUARE_OCCUPANT_FAILURE #======================#
    "AddingSquareOccupantFailedException",
]


# ======================# ADDING_SQUARE_OCCUPANT_FAILURE #======================#
class AddingSquareOccupantFailedException(SquareException, InsertionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a token entering a square failed.

    # PARENT:
        *   SquareException
        *   InsertionFailedException


    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_SQUARE_OCCUPANT_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Token entering a square failed."