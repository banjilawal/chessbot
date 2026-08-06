# src/topology/basis/pawn/maneuver/opening/basis.py

"""
Module: topology.basis.pawn.maneuver.opening.basis
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from collection import VectorSet
from schema import Offset
from basis import PawnManeuverBasis


class OpeningPawnManeuverBasis(PawnManeuverBasis):
    """
    Role:
        -  Data Holder

    Responsibilities:
        1.  Constraints or that are used to generate a RankTree for Opening maneuvering Pawns.

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        PawnManeuverBasis
    """
    
    def __init__(self, offsets: VectorSet = Offset.OPENING_PAWN_MANEUVER.entries ):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(offsets=offsets)
   
    
    
