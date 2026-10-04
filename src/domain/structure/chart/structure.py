# src/domain/struct/chart/struct.py

"""
Module: domain.struct.chart.struct
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any, Dict, Generic, TypeVar

from domain import Model, Struct

T = TypeVar("T", bound="Model")

class Chart(Struct, Generic[T]):
    pass
        
    @property
    def size(self) -> int:
        return len(self.to_dict)
        
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    @abstractmethod
    def is_full(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def consistency_exists(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def is_not_consistent(self) -> bool:
        pass
        
    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass
    
        
        
