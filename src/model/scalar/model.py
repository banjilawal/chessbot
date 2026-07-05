# src/model/scalar/model/state.py

"""
Module: model.scalar.model
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
        *   magnitude (int)

    # INHERITED ATTRIBUTES:
    None

    Attributes:
        *   magnitude (int)

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    None
    """
    _magnitude: int
    
    def __init__(self, magnitude: int):
        self._magnitude = magnitude
    
    @property
    def magnitude(self) -> int:
        return self._magnitude
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Scalar):
            return self._magnitude == other.magnitude
        return False
    
    def __hash__(self):
        return hash(self._magnitude)
    
    def __str__(self):
        return f"Scalar(magnitude={self._magnitude})"
