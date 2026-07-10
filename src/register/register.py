# src/model/register/model/state.py

"""
Module: model.register.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Any, Dict, Generic, List


class Register(ABC, Generic[Any]):
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
    a: Any
    b: Any
    
    def __init__(self, a: Any, b: Any,):
        """
        Args:
            a: T
            b: T
        """
        self._a = a
        self._b = b
    
    @property
    def a(self) -> A:
        return self._a
    
    @property
    def b(self) -> A:
        return self._b
    
    @property
    def to_list(self) -> List[A]:
        return [self._a, self._b]
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {"a": self._a, "v": self._b}