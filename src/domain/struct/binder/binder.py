# src/domain/struct/binder/binder.py

"""
Module: domain.struct.binder.binder
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

class ArchetypeBinder(ABC, Generic[T]):
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
    def consistency_exists(self) -> bool:
        if self is None:
            return False
        if self.is_half_full:
            return False
        if self.entries_are_not_unique:
            return False
        if self.is_full and self.entries_are_unique:
            return True
        return False
    
    @property
    def is_not_consistent(self) -> bool:
        return not self.consistency_exists
    
    @property
    @abstractmethod
    def entries_are_unique(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def entries_are_not_unique(self) -> bool:
        pass
    
    @property
    def size(self) -> int:
        return len(self.to_dict)

    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_full(self) -> bool:
        return self.size == 2
    
    @property
    def is_half_full(self) -> bool:
        return self.size == 1
    
    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, T]:
        pass

        
    