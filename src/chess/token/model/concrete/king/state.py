# src/chess/token/model/concrete/king/state.py

"""
Module: chess.token.model.concrete.king.state
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum, auto

class KingActivityState(Enum):
    FREE = auto(),
    IN_CHECK = auto(),
    CHECKMATED = auto()
