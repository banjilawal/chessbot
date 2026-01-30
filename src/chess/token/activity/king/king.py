# src/chess/token/state/activity/king/king.py

"""
Module: chess.token.state.activity.king.king
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from abc import ABC
from enum import Enum

from chess.token import KingReadiness
from chess.token.activity import ActivityState


class KingActivityState(ActivityState, ABC):
    _classification: Enum
    
    def __init__(self, state: KingReadiness):
        super().__init__(state=state)