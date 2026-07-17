# src/space/span/basis/span.py

"""
Module: space.span.basis.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from model import Vector
from space import DestinationSpanComputer
from space.span import MovementVectorSet

T = TypeVar("T", bound="Rank")

class VectorBasis(ABC, Generic[T]):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destination vectors from an origin by adding it to each
            movement vector.

    Attributes:
        origin: Vector
        movement_vectors: MovementVectorSet[T]
        destination_span_computer: Optional[DestinationSpanComputer]
        
        is_empty: bool
        is_not_empty: bool
        is_a_point: bool
        is_a_line: bool:
        is_an_area:  bool
        has_inconsistency: bool
        
    Provides:

    Super Class:
    """
    _origin: Vector
    _movement_vectors: MovementVectorSet[T]
    _destination_span_computer: DestinationSpanComputer
    
    def __init__(
            self,
            origin: Vector,
            movement_vectors: MovementVectorSet[T],
            destination_span_computer: Optional[DestinationSpanComputer] |
                                       None = DestinationSpanComputer(),
    ):
        """
        Args:
            origin: Vector
            movement_vectors: MovementVectorSet
            destination_span_computer: Optional[DestinationSpanComputer]
        """
        self._origin = origin
        self._movement_vectors = movement_vectors
        self._destination_span_computer = destination_span_computer
        
    @property
    def origin(self) -> Vector:
        return self._origin
    
    @property
    def movement_vectors(self) -> MovementVectorSet[T]:
        return self._movement_vectors
    
    @property
    def destination_span_computer(self) -> DestinationSpanComputer:
        return self._destination_span_computer
    
    @property
    def is_empty(self) -> bool:
        return self._movement_vectors.is_empty and self._origin is None
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    def is_a_point(self) -> bool:
        return self._origin is not None and self._movement_vectors.is_empty
    
    @property
    def is_a_line(self) -> bool:
        return self.origin is not None and self._movement_vectors.size == 1
    
    @property
    def is_an_area(self) -> bool:
        return self._origin is not None and self._movement_vectors.size > 1
    
    @property
    def has_inconsistency(self) -> bool:
        return self.is_a_point or self.is_empty
    

        
