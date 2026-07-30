# src/signature/pawn/maneuver/developed/signature.py

"""
Module: signature.pawn.maneuver.developed.signature
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from container import VectorSet
from schema import Offset
from signature import PawnManeuverSignature


class DevelopedPawnManeuverSignature(PawnManeuverSignature):
    """
    Role:
        -  Data Holder

    Responsibilities:
        1.  Constraints or that are used to generate a RankTree for Developed maneuvering Pawns.

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        PawnManeuverSignature
    """
    def __init__(self, offsets: VectorSet = Offset.DEVELOPED_PAWN_MANEUVER.entries,):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(offsets=offsets)
    
    
