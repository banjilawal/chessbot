# src/toolkit/builder/model/model/number/toolkit.py

"""
Module: toolkit.builder.model.model.number.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, List, cast

from model import ModelModel


class NumberModel(ModelModel[int]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the endpoints of a journey.

    Attributes:
        a: int
        b: int
        a_is_b: bool
        a_is_not_b: bool
            
    Provides:

    Super Class:
        Model
    """
    
    def __init__(self, a: int, b: int,):
        """
        Args:
            a: int
            b: int
        """
        super().__init__(a=a, b=b)
        
    @property
    def a(self) -> int:
        return cast(int, self.a)
    
    @property
    def b(self) -> int:
        return cast(int, self.b)

    @property
    def a_is_b(self) -> bool:
        return self.a == self.b
    
    @property
    def a_is_not_b(self) -> bool:
        return not self.a_is_b
    
    @property
    def to_list(self) -> List[int]:
        return [self.a, self.b]
    
    @property
    def to_dict(self) -> Dict[str, int]:
        return {
            "a": self.a,
            "b": self.b,
        }
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, NumberModel):
            return (
                    self._a == other.a and
                    self._b == other.b
            )
    
