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

from domain import Archetype, Archetyped, Struct

T = TypeVar("T", bound="Archetyped")

class ArchetypeBinder(Struct, ABC, Generic[T]):
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
    
    _white_entry: T
    _black_entry: T
    
    
    def __init__(self, white_entry: T, black_entry: T):
        self._white_entry = white_entry
        self._black_entry = black_entry
        
    @property
    def white_entry(self) -> T:
        return self._white_entry
    
    @property
    def black_entry(self) -> T:
        return self._black_entry
    
    @property
    def size(self) -> int:
        return len(self.bindings)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    def archetypes_are_the_same(self) -> bool:
        return self._white_entry.archetype == self._black_entry.archetype
    
    @property
    def archetypes_differ(self) -> bool:
        return not self.archetypes_are_the_same
    
    @property
    def is_balanced(self) -> bool:
        return (
                self is not None and
                super().is_balanced and
                self.entries_are_unique and
                self.archetypes_differ
        )
    
    @property
    @abstractmethod
    def is_not_balanced(self) -> bool:
        return not self.is_balanced

    @property
    def consistency_exists(self) -> bool:
        return (
                self.is_balanced and
                self._white_entry.archetype == Archetype.WHITE and
                self._black_entry.archetype == Archetype.BLACK
        )
    
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
    @abstractmethod
    def bindings(self) -> Dict[Archetype, T]:
        pass
        
    @property
    def to_dict(self) -> Dict[str, T]:
        return {
            "white": self._white_entry,
            "black": self._black_entry
        }

        
    