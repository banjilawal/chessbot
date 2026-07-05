# src/model/register/model/state.py

"""
Module: model.register.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, Generic, List, TypeVar

from model import Model

T = TypeVar("T")


class Register(Model, Generic[T]):
    """
    Role:
        -   Addressing
        -   Data-Holder
  
    Responsibilities:
        1.  Contains a pair used in a binary operation whose operands must have
            the same type.
        
    Attributes:
        a: int
        b: int
        to_list: List[T]:
        to_dict: Dict[str, T]:
        
    Provides:
    
    Super Class:
        Model
    """
    a: T
    b: T
    
    def __init__(self, a: T, b:T,):
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
    def to_list(self) -> List[T]:
        return [self._a, self._b]
    
    @property
    def to_dict(self) -> Dict[str, T]:
        return {"a": self._a, "v": self._b}