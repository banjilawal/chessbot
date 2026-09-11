# src/domain/model/searchable/state/token/state/readiness.py

"""
Module: domain.model.searchable.state.token.state.readiness
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from enum import Enum, auto


class KingReadiness(Enum):
    """
    Role:
        - State
    
    Responsibilities:
        1.  Indicating a KingToken's state during the game.
    
    Attributes:
    
    Provides:
    
    Super Class:
        Enum
    """
    READY = auto(),
    IN_CHECK = auto(),
    CHECKMATED = auto(),