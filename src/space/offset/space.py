# src/space/offset/space.py

"""
Module: space.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Iterator, TypeVar

from container import VectorSet
from model import Vector
from space import MovementPattern

T = TypeVar("T", bound="Rank")

class OffsetPattern(MovementPattern, Generic[T]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Provide a set of vectors that are each added to an origin to produce a span of destination
            vectors.

    Attributes:
        offsets: DeltaSet

    Provides:

    Super Class:
    """
    _offsets: VectorSet
    
    def __init__(self, offsets: VectorSet, ):
        """
        Args:
            offsets: VectorSet
        """
        self._offsets = offsets

    @property
    def iterator(self) -> Iterator[Vector]:
        return self._offsets.iterator
    
    @property
    def size(self) -> int:
        return self._offsets.size
    
    @property
    def is_empty(self) -> bool:
        return self._offsets.is_empty
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    def is_a_point(self) -> bool:
        return self._offsets.size == 1
    
    