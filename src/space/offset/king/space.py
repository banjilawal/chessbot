# src/space/offset/king/space.py

"""
Module: space.offset.king.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from container import VectorSet
from model import King, Vector
from schema import Offset
from space import OffsetPattern


class KingOffsetPattern(OffsetPattern[King]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  The second component of a KingBasis. Necessary for computing a KingToken's destination vectors.

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        ManeuverVectorSet
    """
    
    def __init__(self, offsets: VectorSet = Offset.entries):
        """
        Args:t
        """
        super().__init__(offsets=offsets)
    
