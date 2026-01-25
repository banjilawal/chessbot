# src/chess/token/state/activity/abstract.py

"""
Module: chess.token.state.activity.abstract
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from abc import ABC
from enum import Enum


class ActivityState(ABC):
    _state: Enum
    
    def __init__(self, state: Enum):
        self._state = state
    
    @property
    def state(self) -> Enum:
        pass
    
    @state.setter
    def state(self, state: Enum):
        pass
    
    