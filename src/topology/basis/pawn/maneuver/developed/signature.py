# src/topology/basis/pawn/maneuver/developed/basis.py

"""
Module: topology.basis.pawn.maneuver.developed.basis
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from collection import VectorSet
from schema import Offset
from basis import PawnManeuverBasis


class DevelopedPawnManeuverBasis(PawnManeuverBasis):
    """
    Role:
        -  Data Holder

    Responsibilities:
        1.  Constraints or that are used to generate a RankTree for Developed maneuvering Pawns.

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        PawnManeuverBasis
    """
    def __init__(self, offsets: VectorSet = Offset.DEVELOPED_PAWN_MANEUVER.entries,):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(offsets=offsets)
    
    
