# src/container/vector/destination/container.py

"""
Module: container.vector.destination.container
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import  Optional, Tuple

from container import VectorSet
from model import Vector


class DestinationVectorSet(ABC, VectorSet):
    """
    Role:
        -   Data Holder
        
    Responsibilities:
        1.  Store Vectors that have a common root.
        2.  Stores the output of SpanSteppers or DestinationSpanComputers.

    Attributes:
        root: Vector
        entries: Optional[Tuple[Vector, ...]]

    Provides:

    Super Class:
        VectorSet
    """
    _root: Vector
    
    def __init__(
            self,
            root: Vector,
            entries: Optional[Tuple[Vector, ...]] | None = None
    ):
        """
        Args:
            root: Vector
            entries: Optional[Tuple[Vector, ...]]
        """
        super().__init__(entries=entries)
        self._root = root
        
    @property
    def root(self) -> Vector:
        return self._vetor

        