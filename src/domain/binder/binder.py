# src/domain/binder/binder.py

"""
Module: domain.binder.binder
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, Optional, TypeVar

from config import GameColor
from domain import Model

P = TypeVar("P", bound="Model")
S = TypeVar("S", bound="Model")

class ColorBinder(ABC, Generic[P, S]):
    """
    Role:
        - Mapper
        
    Responsibility:
        1.  Create a biding between GameColor and two entities that have a one-to-many
            relationship.
        
    Attributes:
        id: int
        max_capacity: int
        
    Provides:

    Super Class:
        Structure
    """
    MAX_CAPACITY = 2
    
    _id: int
    _primary: P
    _max_capacity: int
    
    def __init__(
            self,
            id: int,
            primary: P,
            max_capacity: Optional[int] | None = None,
    ):
        """
        Args:
            id: int
            max_capacity: Optional[int]
        """
        self._id = id
        self._primary = primary
        self._max_capacity = max_capacity or self.MAX_CAPACITY
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def primary(self) -> P:
        return self._primary
    
    @property
    def max_capacity(self) -> int:
        return self._max_capacity
    
    @property
    def size(self) -> int:
        return len(self.to_dict)

    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_correct_size(self) -> bool:
        return self.size == self._max_capacity
    
    @property
    def over_capacity(self) -> bool:
        return self.size > self._max_capacity
    
    @property
    @abstractmethod
    def to_dict(self) -> Dict[GameColor, S]:
        pass
    
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ColorBinder):
            return self.id == other.id
        return False
        
    def __hash__(self):
        return hash(self.id)

        
    