# src/domain/struct/struct.py

"""
Module: domain.struct.struct
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, TypeVar

from domain import SearchableModel

T = TypeVar("T", bound="SearchableModel")


class Struct(ABC, Generic[T]):
    """
    Role:
        - Structural

    Responsibility:
        1.  Provides struct and additional capabilities to a pure data object.

    Attributes:

    Provides:

    Super Class:
    """
    
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
    def is_balanced(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def is_not_balanced(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, T]:
        pass

    