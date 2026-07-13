# src/register/model/cartesian/register.py

"""
Module: register.model.cartesian.register
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, List

from chooser import CartesianPoint
from register import ModelRegister


class CartesianRegister(ModelRegister[CartesianPoint]):
    """
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains CartesianPoints passed for Vector Algebra

    Attributes:
        a: CartesianPoint
        b: CartesianPoint

        is_vector_register:bool
        is_coord_register: bool
        to_list: List[Cartesian]
        to_dict: Dict[str, Cartesian]

    Super Class:
        Register
    """
    
    def __init__(
            self,
            a: CartesianPoint,
            b: CartesianPoint,
    ):
        """
        Args:
            a: CartesianPoint
            b: CartesianPoint
        """
        super().__init__(a=a, b=b)
        
    @property
    def a(self) -> CartesianPoint:
        return self._a
    
    @property
    def b(self) -> CartesianPoint:
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
    
    @property
    def to_list(self) -> List[CartesianPoint]:
        return [self.a, self.b]
    
    @property
    def to_dict(self) -> Dict[str, CartesianPoint]:
        return {
            "a": self.a,
            "b": self.b,
        }
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CartesianRegister):
            return (
                    self._a == other.b and
                    self._b == other.b
            )
    
    
    
