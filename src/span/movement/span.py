# src/span/movement/span.py

"""
Module: span.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic,  TypeVar

from container import VectorSet
from model import Vector

T = TypeVar("T", bound="Rank")

class MovementVectorSet(ABC, Generic[T]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Store upper and lower movement of a Span. basic integrity and sanity checking.

    Attributes:
        movement_vectors: DeltaSet

    Provides:

    Super Class:
    """
    _movement_vectors: VectorSet
    
    def __init__(self, movement_vectors: VectorSet,):
        """
        Args:
            movement_vectors: VectorSet
        """
        self._movement_vectors = movement_vectors
    
    @property
    def movement_vectors(self) -> VectorSet:
        return self._movement_vectors
