# src/domain/model/searchable/state/token/state/board.py

"""
Module: domain.model.searchable.state.token.state.board
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from enum import Enum, auto

class TokenDeployment(Enum):
    """
    Role:
        - State

    Responsibilities:
        1.  Indicating the token has been deployed to its HomeSquare
        
    Attributes:
    
    Provides:

    Super Class:
        Enum
    """
    NOT_DEPLOYED = auto(),
    DEPLOYED_TO_HOME_SQUARE = auto(),