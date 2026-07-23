# src/space/basis/basis/pawn/maneuver/developed/space.py

"""
Module: space.basis.basis.pawn.maneuver.developed.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from model import Vector
from space import VectorTargetingComputer, DevelopedManeuverOffsetPattern, PawnManeuverVectorBasis


class DevelopedPawnManeuverVectorBasis(PawnManeuverVectorBasis):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destination vectors for a Pawn which has not made its developed move.

    Attributes:
        origin: Vector
        offsets: Optional[DevelopedVectorSet]
        targeting_computer: Optional[DestinationSpanComputer]
            
    Provides:

    Super Class:
        PawnManeuverVectorBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            offsets: Optional[DevelopedManeuverOffsetPattern] |
                              None = DevelopedManeuverOffsetPattern(),
            targeting_computer: Optional[VectorTargetingComputer] |
                                None = VectorTargetingComputer(),
    ):
        """
        Args:
            origin: Vector
            offsets: Optional[DevelopedVectorSet]
            targeting_computer: Optional[DestinationSpanComputer]
        """
        super().__init__(
            origin=origin,
            offsets=offsets,
            targeting_computer=targeting_computer,
        )

