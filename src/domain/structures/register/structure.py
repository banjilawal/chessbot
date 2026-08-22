# src/domain/structures/register/structure.py

"""
Module: domain.structures.register.structure
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Dict, Generic, List, Optional, TypeVar

from domain import DomainObject, StructuralWrapper

T = TypeVar("T", bound="DomainObject")


class Register(StructuralWrapper, ABC, Generic[T]):
    """
    Role:
        -   Addressing
        -   Data-Holder
  
    Responsibilities:
        1.  Contains a pair used in a binary operation whose operands must have
            the same type.
        
    Attributes:
        a: T
        b: T
        id: Optional[int]
        to_list: List[T]
        to_dict: Dict[str, T]
        
    Provides:
    
    Super Class:
        Model
    """
    _a: T
    _b: T
    _id: Optional[int]
    
    def __init__(self, a: T, b: T, id: Optional[int] | None = None):
        """
        Args:
            a: T
            b: T
            id: Optional[int]
        """
        self._a = a
        self._b = b
        self._id = id
    
    @property
    def a(self) -> T:
        return self._a
    
    @property
    def b(self) -> T:
        return self._b
    
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def to_list(self) -> List[T]:
        return [self._a, self._b]
    
    @property
    def to_dict(self) -> Dict[str, T]:
        return {"a": self._a, "v": self._b}
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_right_size(self) -> bool:
        return self.size == 2
    
    @property
    def is_wrong_size(self) -> bool:
        return not (
                self.is_empty and self.is_right_size
        )
    
    @property
    def size(self) -> int:
        return len(self.to_list)