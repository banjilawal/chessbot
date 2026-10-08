# src/domain/model/alert/level.py

"""
Module: domain.model.alert.level
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from enum import Enum, auto


class ThreatLevel(Enum):
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