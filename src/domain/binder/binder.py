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
from domain import Model

T = TypeVar("T", bound="Model")

class ColorBinder(ABC, Generic[T]):
    """
    Role:
        - Mapper
        
    Responsibility:
        1.  Create a biding between GameColor and two entities that have a one-to-many
            relationship.
        
    Attributes:
        max_capacity: int
        
    Provides:

    Super Class:
        Structure
    """
    _MAX_CAPACITY = 2
    _white_item: T
    _black_item: T
    
    def __init__(
            self,
            white_item: T,
            black_item: T,
    ):
        """
        Args:
            white_item: T
            black_item: T
        """
        self._white_item = white_item
        self._black_item = black_item
    
    @property
    def white_item(self) -> T:
        return self._white_item
    
    @property
    def black_item(self) -> T:
        return self._black_item
    
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
    def is_over_capacity(self) -> bool:
        return self.size > self._MAX_CAPACITY
    
    @property
    @abstractmethod
    def to_dict(self) -> Dict[GameColor, T]:
        pass

        
    