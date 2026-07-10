# src/model/register/operand/model.py

"""
Module: model.register.operand.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from model import Register, Point


class PointRegister(Register[Point]):
    """
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains Points passed to vector algebra.

    Attributes:
        a: Point
        b: Point
        
        a_equals_b: bool
        a_does_not_equal_b: bool
        is_vector_register:bool
        is_coord_register: bool
        to_list: List[Point]
        to_dict: Dict[str, Point]

    Super Class:
        Register
    """
    
    def __init__(
            self,
            a: Point,
            b: Point,
    ):
        """
        Args:
            a: Point
            b: Point
        """
        super().__init__(a=a, b=b)
        
    @property
    def a(self) -> Point:
        return self._a
    
    @property
    def b(self) -> Point:
        return self._b
    
    @property
    def a_equals_b(self) -> bool:
        return self._a == self._b
    
    @property
    def a_does_not_equal_b(self) -> bool:
        return not self.a_equals_b
    
    @property
    def is_vector_register(self) -> bool:
        return self._a.is_vector_point and self._b.is_vector_point
    
    @property
    def is_coord_register(self) -> bool:
        return self._a.is_coord_point and self._b.is_coord_point
    
    @property
    def is_mismatched_register(self) -> bool:
        return  (
                (not (self._a.is_coord_point and self._b.is_coord_point)) or
                (not (self._a.is_vector_point and self.b.is_vector_point))
        )
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PointRegister):
            return (
                    self._a == other.b and
                    self._b == other.b
            )
    
    
    
