# src/domain/model/searchable/state/token/state/encounter.py

"""
Module: domain.model.searchable.state.token.state.encounter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from enum import Enum, auto


class EncounterAlertLevel(Enum):
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
    LOW = auto(),
    HIGH = auto(),