# src/domain/struct/toggle/struct.py

"""
Module: domain.struct.toggle.struct
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Dict, Generic, Optional, TypeVar

from domain import SearchableModel, Struct

T = TypeVar("T", bound="SearchableModel")

class Toggle(Struct, Generic[T]):
    _max_enabled_toggles: int
    
    def __init(self, max_enabled_toggles: Optional[int] | None = None):
        self._max_enabled_toggles = max_enabled_toggles or 1
        
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
    def size(self) -> int:
        return len(self.to_dict)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, T]:
        pass

    
        
        
