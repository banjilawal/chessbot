# src/signature/offset/knight/signature.py

"""
Module: signature.offset.knight.signature
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from container import VectorSet
from model import Knight
from schema import Offset
from signature import OffsetSignature


class KnightSignature(OffsetSignature[Knight]):
    """
    Role:
        -   Data Holder
        -   Immutability

    Responsibilities:
        1.  Determine potential destinations from a Knight's current position.

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        OffsetSignature
    """
    
    def __init__(self,  offsets: VectorSet = Offset.KNIGHT.entries):
        """
        """
        super().__init__(offsets=offsets)
    
