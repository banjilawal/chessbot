# src/geometry/scalar/model.py

"""
Module: geometry.scalar.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class Scalar:
    """
    Role:Computation, Transformation, Data-Holder
    
    Responsibilities:
    1.  A 1-D quantity.
    2.  Creating new 2-D object which can be either a
            *   Vector
            *   Coords
        by multiplying an originating 2-D by the scalar.

    Super Class:
    None

    Provides:

    # LOCAL ATTRIBUTES:
        *   value (int)

    # INHERITED ATTRIBUTES:
    None

    Attributes:
        *   value (int)

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    None
    """
    _value: int
    
    def __init__(self, value: int):
        self._value = value
    
    @property
    def value(self) -> int:
        return self._value
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Scalar):
            return self._value == other.value
        return False
    
    def __hash__(self):
        return hash(self._value)
    
    def __str__(self):
        return f"Scalar(value={self._value})"
