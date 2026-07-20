# src/space/span/maneuver/span.py

"""
Module: space.span.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Iterator, TypeVar

from container import VectorSet
from model import Vector

T = TypeVar("T", bound="Rank")

class ManeuverVectorSet(ABC, Generic[T]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Provide a set of vectors that are each added to an origin to produce a span of destination
            vectors.

    Attributes:
        maneuver_vectors: DeltaSet

    Provides:

    Super Class:
    """
    _maneuver_vectors: VectorSet
    
    def __init__(self, maneuver_vectors: VectorSet,):
        """
        Args:
            maneuver_vectors: VectorSet
        """
        self._maneuver_vectors = maneuver_vectors

    @property
    def iterator(self) -> Iterator[Vector]:
        return self._maneuver_vectors.iterator
    
    @property
    def size(self) -> int:
        return self._maneuver_vectors.size
    
    @property
    def is_empty(self) -> bool:
        return self._maneuver_vectors.is_empty
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    def is_a_point(self) -> bool:
        return self._maneuver_vectors.size == 1
    
    