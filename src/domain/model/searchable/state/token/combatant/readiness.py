# src/domain/model/searchable/state/token/state/readiness.py

"""
Module: domain.model.searchable.state.token.state.readiness
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from enum import Enum, auto


class CombatantReadiness(Enum):
    """
    Role:
        - State
    
    Responsibilities:
        1.  Indicating a CombatantToken's state during the game.
    
    Attributes:
    
    Provides:
    
    Super Class:
        Enum
    """
    READY = auto(),
    CAPTURED = auto(),
    OFF_BOARD = auto(),
    