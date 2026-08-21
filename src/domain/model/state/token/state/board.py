# src/dossier/model/state/token/state/board.py

"""
Module: domain.model.state.token.state.board
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from enum import Enum, auto

class DeploymentState(Enum):
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
    NOT_DEPLOYED = auto(),
    DEPLOYED = auto(),
    REMOVED_FROM_BOARD = auto(),