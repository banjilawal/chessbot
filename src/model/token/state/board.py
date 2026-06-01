# src/model/token/state/board.py

"""
Module: model.token.state.board
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import Enum, auto

class TokenBoardState(Enum):
    """
    Role:
        -   State

    Responsibilities:
        1.  Describes Token's relationship with the Board.
        
    Attributes:
    
    Provides:

    Super Class:
        Enum
    """
    HAS_NOT_DEPLOYED = auto(),
    CLAIMED_HOME_SQUARE = auto(),
    REMOVED_FROM_BOARD = auto(),