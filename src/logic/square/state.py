# src/logic/square/state.py

"""
Module: logic.square.state
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum, auto


class SquareState(Enum):
    """
    # ROLE: State Descriptor

    # RESPONSIBILITIES:
    1.  Indicating if the Token is in a state where
            *   It has not been deployed to its opening square.
            *   II has been deployed on the board.
            *   It has been removed from the board.

    # PARENT:
        Enum

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   NEVER_BEEN_PLACED
        *   DEPLOYED_ON_BOARD
        *   REMOVED_FROM_BOARD

    # INHERITED ATTRIBUTES:
        *   See Enum class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
   None

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See Enum class for inherited methods.
    """
    EMPTY = auto(),
    OCCUPIED = auto(),
    TOKEN_ENTERING = auto(),
    DEPARTING_TOKEN = auto(),
    DOUBLE_COMBATANT_OCCUPANCY = auto(),