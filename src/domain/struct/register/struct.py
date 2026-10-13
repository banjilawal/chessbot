# src/domain/struct/register/struct.py

"""
Module: domain.struct.register.struct
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, List, Optional, TypeVar

from domain import SearchableModel, Struct

T = TypeVar("T", bound="SearchableModel")


class Register(Struct, ABC, Generic[T]):
    """
    Role:
        - Addressing
        - Data-Holder
  
    Responsibilities:
        1.  Contains a pair used in a binary operation whose operands must have
            the same type.
        2.  Centralizes tests for
                - uniqueness
                - nulls
                - size
        
    Attributes:
        a: T
        b: T
        
    Provides:
    
    Super Class:
        Struct
    """
    _a: T
    _b: T
    
    def __init__(self, a: T, b: T):
        """
        Args:
            a: T
            b: T
        """
        self._a = a
        self._b = b
    
    @property
    def a(self) -> T:
        return self._a
    
    @property
    def b(self) -> T:
        return self._b
    
    @property
    @abstractmethod
    def a_is_b(self) -> bool:
        pass
    
    @property
    def a_is_not_b(self) -> bool:
        return not self.a_is_b
    
    @property
    def is_balanced(self) -> bool:
        return self.size == 2
    
    @property
    def is_not_balanced(self) -> bool:
        return self.size == 1
    
    @property
    def consistency_exists(self) -> bool:
        if (
                self is None or
                self.is_empty or
                self.is_not_balanced
        ):
            return False
        return True
    
    @property
    def is_not_consistent(self) -> bool:
        return not self.consistency_exists
    
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
    def to_dict(self) -> Dict[str, T]:
        return {"a": self._a, "b": self._b}
    

    
