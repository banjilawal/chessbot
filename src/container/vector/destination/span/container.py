# src/container/vector/destination/span/container.py

"""
Module: container.vector.destination.span.container
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import  Optional, Tuple

from container import DestinationVectorSet
from model import Vector


class SpanDestinationSet(DestinationVectorSet):
    """
    Role:
        -   Data Holder
        
    Responsibilities:
        1.  Store root and destination vectors from spanning a basis set.

    Attributes:
        root: Vector
        entries: Optional[Tuple[Vector, ...]]
        
    Provides:

    Super Class:
        DestinationVectorSet
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
        super().__init__(root=root, entries=entries)

        