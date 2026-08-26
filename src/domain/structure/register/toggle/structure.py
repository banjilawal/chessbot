# src/domain/structure/register/vector_toggle/structure.py

"""
Module: domain.structure.register.vector_toggle.structure
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, List, cast

from domain import CartesianToggle, Register


class CartesianToggleRegister(Register[CartesianToggle]):
    """
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains VectorToggles passed for Vector Algebra

    Attributes:
        a: VectorToggle
        b: VectorToggle

        is_vector_register:bool
        is_coord_register: bool
        to_list: List[Vectortoggle]
        to_dict: Dict[str, Vectortoggle]

    Super Class:
        Register
    """
    
    def __init__(
            self,
            u: CartesianToggle,
            v: CartesianToggle,
    ):
        """
        Args:
            u: VectorToggle
            v: VectorToggle
        """
        super().__init__(a=u, b=v)
    
    @property
    def u(self) -> CartesianToggle:
        return cast(CartesianToggle, super().a)
    
    @property
    def v(self) -> CartesianToggle:
        return cast(CartesianToggle, super().b)
        
    @property
    def a(self) -> CartesianToggle:
        return self.u
    
    @property
    def b(self) -> CartesianToggle:
        return self.v
    
    @property
    def b(self) -> CartesianToggle:
        return self._b
    
    @property
    def a_equals_b(self) -> bool:
        return self._a == self._b
    
    @property
    def a_does_not_equal_b(self) -> bool:
        return not self.a_equals_b
    
    @property
    def is_vector_register(self) -> bool:
        return self._a.is_vector_toggle and self._b.is_vector_toggle
    
    @property
    def is_coord_register(self) -> bool:
        return self._a.is_coord_toggle and self._b.is_coord_toggle

    @property
    def toggles_are_carrying_different_types(self) -> bool:
        return (
            not self.is_vector_register and
            not self.is_coord_register
            
        )
    
    @property
    def to_list(self) -> List[CartesianToggle]:
        return [self.a, self.b]
    
    @property
    def to_dict(self) -> Dict[str, CartesianToggle]:
        return {
            "a": self.a,
            "b": self.b,
        }
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CartesianToggleRegister):
            return (
                    self._a == other.b and
                    self._b == other.b
            )
    
    
    
