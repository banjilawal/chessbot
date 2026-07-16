# src/span/basis/span.py

"""
Module: span.basis.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from model import Vector
from span import VectorSet

T = TypeVar("T", bound="Rank")

class VectorBasis(ABC, Generic[T]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Store upper and lower basis of a Span. basic integrity and sanity checking.

    Attributes:
        origin: Vector
        movement_vectors: DeltaSet

    Provides:

    Super Class:
    """
    _origin: Vector
    _movement_vectors: VectorSet
    
    def __init__(self, origin: Vector, movement_vectors: VectorSet,):
        """
        Args:
            origin: Vector
            movement_vectors: DeltaSet
        """
        self._origin = origin
        self._movement_vectors = movement_vectors
        
    @property
    def origin(self) -> Vector:
        return self._origin
    
    @property
    def movement_vectors(self) -> VectorSet[T]:
        return self._movement_vectors
    
    @property
    def is_empty(self) -> bool:
        return self._movement_vectors.is_empty and self._origin is None
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    def is_a_line(self) -> bool:
        return self.origin is not None and self._movement_vectors.is_a_point
    
    @property
    def is_an_area(self):
        return self._origin is not None and self._movement_vectors.is_linear
