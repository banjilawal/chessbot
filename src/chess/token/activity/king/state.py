# src/chess/token/state/activity/king/state.py

"""
Module: chess.token.state.activity.king.state
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from enum import Enum, auto

class KingState(Enum):
    FREE = auto(),
    IN_CHECK = auto(),
    CHECKMATED = auto()
