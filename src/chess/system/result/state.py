# src/chess/system/result/state.py

"""
Module: chess.system.result.state
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from abc import ABC
from typing import Generic, TypeVar

T = TypeVar("T")

class ResultState(ABC, Generic[T]):
    _classification: T
    
    def __init__(self, classification: T):
        self._classification = classification

    @property
    def classification(self) -> T:
        return self._classification