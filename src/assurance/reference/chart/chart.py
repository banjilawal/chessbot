# src/assurance/reference/chart/chart.py

"""
Module: assurance.reference.chart.chart
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, TypeVar

from domain import Model

T = TypeVar("T", bound="Model")

class ValidatorChart(ABC, Generic[T]):
    
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
    def to_dict(self) -> Dict[str, T]:
        pass


