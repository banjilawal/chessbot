# src/domain/structure/register/vector_toggle/structure.py

"""
Module: domain.structure.register.vector_toggle.structure
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, List, cast

from domain import Cartesian, Register


class CartesianRegister(Register[Cartesian]):
    """
        - Model
        - Data Holder

    Responsibilities:
        1.  Contains Cartesian passed for Vector Algebra

    Attributes:
        a: Cartesian
        b: Cartesian

        is_vector_register:bool
        is_coord_register: bool
        to_list: List[Cartesian]
        to_dict: Dict[str, Cartesian]

    Super Class:
        Register
    """
    
    def __init__(
            self,
            u: Cartesian,
            v: Cartesian,
    ):
        """
        Args:
            u: Cartesian
            v: Cartesian
        """
        super().__init__(a=u, b=v)
    
    @property
    def u(self) -> Cartesian:
        return cast(Cartesian, super().a)
    
    @property
    def v(self) -> Cartesian:
        return cast(Cartesian, super().b)
        
    @property
    def a(self) -> Cartesian:
        return self.u
    
    @property
    def b(self) -> Cartesian:
        return self.v
    
    @property
    def b(self) -> Cartesian:
        return self._b
    
    @property
    def a_equals_b(self) -> bool:
        return self._a == self._b
    
    @property
    def a_does_not_equal_b(self) -> bool:
        return not self.a_equals_b
    
    @property
    def is_vector_register(self) -> bool:
        return self._a.is_vector_locus and self._b.is_vector_locus
    
    @property
    def is_coord_register(self) -> bool:
        return self._a.is_coord_locus and self._b.is_coord_locus

    @property
    def is_mismatched(self) -> bool:
        return (
            not self.is_vector_register and
            not self.is_coord_register
        )
    
    @property
    def to_list(self) -> List[Cartesian]:
        return [self.a, self.b]
    
    @property
    def to_dict(self) -> Dict[str, Cartesian]:
        return {
            "a": self.a,
            "b": self.b,
        }
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, CartesianRegister):
            return (
                    self._a == other.b and
                    self._b == other.b
            )
        return False
    
    
    
