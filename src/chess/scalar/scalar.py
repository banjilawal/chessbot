# src/chess/scalar/scalar.py


"""
Module: chess.scalar.scalar
Author: Banji Lawal
Created: 2025-09-11
version: 1.0.0
"""

from __future__ import annotations


class Scalar:
    """
    # ROLE: Computation, Transformation, Data-Holder
    
    # RESPONSIBILITIES:
    1.  A 1-D quantity.
    2.  Creates new 2-D object which can be either a
            *   Vector
            *   Coords
        by multiplying an originating 2-D by the scalar.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   value (int)

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
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
