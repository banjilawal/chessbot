# src/toolkit/builder/model/model/vector_toggle/toolkit.py

"""
Module: toolkit.builder.model.model.vector_toggle.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, List, cast

from model import ModelModel
from toggle import VectorToggle


class VectorToggleModel(ModelModel[VectorToggle]):
    """
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains VectorToggles passed for Vector Algebra

    Attributes:
        a: VectorToggle
        b: VectorToggle

        is_vector_model:bool
        is_coord_model: bool
        to_list: List[Vectortoggle]
        to_dict: Dict[str, Vectortoggle]

    Super Class:
        Model
    """
    
    def __init__(
            self,
            u: VectorToggle,
            v: VectorToggle,
    ):
        """
        Args:
            u: VectorToggle
            v: VectorToggle
        """
        super().__init__(a=u, b=v)
    
    @property
    def u(self) -> VectorToggle:
        return cast(VectorToggle, super().a)
    
    @property
    def v(self) -> VectorToggle:
        return cast(VectorToggle, super().b)
        
    @property
    def a(self) -> VectorToggle:
        return self.u
    
    @property
    def b(self) -> VectorToggle:
        return self.v
    
    @property
    def b(self) -> VectorToggle:
        return self._b
    
    @property
    def a_equals_b(self) -> bool:
        return self._a == self._b
    
    @property
    def a_does_not_equal_b(self) -> bool:
        return not self.a_equals_b
    
    @property
    def is_vector_model(self) -> bool:
        return self._a.is_vector_toggle and self._b.is_vector_toggle
    
    @property
    def is_coord_model(self) -> bool:
        return self._a.is_coord_toggle and self._b.is_coord_toggle

    @property
    def toggles_are_carrying_different_types(self) -> bool:
        return (
            not self.is_vector_model and
            not self.is_coord_model
            
        )
    
    @property
    def to_list(self) -> List[VectorToggle]:
        return [self.a, self.b]
    
    @property
    def to_dict(self) -> Dict[str, VectorToggle]:
        return {
            "a": self.a,
            "b": self.b,
        }
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorToggleModel):
            return (
                    self._a == other.b and
                    self._b == other.b
            )
    
    
    
