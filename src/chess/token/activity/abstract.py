# src/chess/token/state/activity/abstract.py

"""
Module: chess.token.state.activity.abstract
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from abc import ABC
from enum import Enum


class ActivityState(ABC):
    _classification: Enum
    
    def __init__(self, classification: Enum):
        self._classification = classification
    
    @property
    def classification(self) -> Enum:
        return self._classification
    
    @classification.setter
    def classification(self, classification: Enum):
        self._classification = classification
    