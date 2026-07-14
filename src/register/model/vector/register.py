# src/register/model/vector/register.py

"""
Module: register.model.vector.register
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, List, cast

from model import Vector
from register import ModelRegister


class VectorRegister(ModelRegister[Vector]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the endpoints of a journey.

    Attributes:
        u: Vector
        v: Vector
        u_is_v: bool
        u_is_not_v: bool
            
    Provides:

    Super Class:
        Register
    """
    _u: Vector
    _v: Vector
    
    def __init__(self, u: Vector, v: Vector,):
        """
        Args:
            u: Vector
            v: Vector
        """
        super().__init__(a=u, b=v)
        
    @property
    def u(self) -> Vector:
        return cast(Vector, self.a)
    
    @property
    def v(self) -> Vector:
        return cast(Vector, self.b)

    @property
    def u_is_v(self) -> bool:
        return self.u == self.v
    
    @property
    def u_is_not_v(self) -> bool:
        return not self.u_is_v
    
    @property
    def to_list(self) -> List[Vector]:
        return [self.u, self.v]
    
    @property
    def to_dict(self) -> Dict[str, Vector]:
        return {
            "u": self.u,
            "v": self.v,
        }
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorRegister):
            return (
                    self._u == other.u and
                    self._v == other.v
            )
    
