# src/toggle/toggle.py

"""
Module: toggle.toggle
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, TypeVar

T = TypeVar("T")

class Toggle(ABC):

    _max_enabled_toggles: int
    
    def __init(self, max_enabled_toggles: int | None = 1):
        self._max_enabled_toggles = max_enabled_toggles
        
    @property
    def max_enabled_toggles(self) -> int:
        return self._max_enabled_toggles
        
    @property
    def no_active_toggles(self) -> bool:
        return self.active_toggles == 0
    
    @property
    def excess_active_toggles(self) -> bool:
        return self.active_toggles > self._max_enabled_toggles
    
    @property
    def active_toggles(self) -> int:
        return len(self.to_dict)
        
    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass
    
        
        
