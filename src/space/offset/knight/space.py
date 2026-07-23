# src/space/offset/knight/space.py

"""
Module: space.offset.knight.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from container import VectorSet
from model import Knight
from schema import Offset
from space import OffsetPattern


class KnightOffsetPattern(OffsetPattern[Knight]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  The second component of a KnightBasis. Necessary for computing a KnightToken's destination vectors.

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        OffsetPattern
    """
    
    def __init__(self,  offsets: VectorSet = Offset.KNIGHT.entries):
        """
        """
        super().__init__(offsets=offsets)
    
