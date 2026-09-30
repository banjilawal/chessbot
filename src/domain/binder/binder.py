# src/domain/binder/binder.py

"""
Module: domain.binder.binder
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, TypeVar

from config import GameColor
from domain import Archetype, Model

T = TypeVar("T", bound="Model")

class ColorBinder(ABC, Generic[T]):
    """
    Role:
        - Mapper
        
    Responsibility:
        1.  Use GameColor to map Model to Archetype.
        
    Attributes:
        size: int
        is_empty: bool
        is_correct_size: bool
        is_not_consistent: bool
        
    Provides:
        same_items: bool
        items_are_different: bool
        to_dict: Dict[GameColor, Dict[Archetype, T]]

    Super Class:
    """
    _MAX_CAPACITY = 2

    @property
    @abstractmethod
    def same_items(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def items_are_different(self) -> bool:
        pass
    
    @property
    def size(self) -> int:
        return len(self.to_dict)

    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_correct_size(self) -> bool:
        return self.size == self._MAX_CAPACITY
    
    @property
    def is_not_consistent(self) -> bool:
        return self.size > self._MAX_CAPACITY
    
    @property
    @abstractmethod
    def to_dict(self) -> Dict[GameColor, Dict[Archetype, T]]:
        pass

        
    