# src/space/basis/basis/pawn/maneuver/opening/space.py

"""
Module: space.basis.basis.pawn.maneuver.opening.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from model import Vector
from space import VectorTargetingComputer, OpeningManeuverOffsetPattern, PawnManeuverVectorBasis


class OpeningPawnManeuverVectorBasis(PawnManeuverVectorBasis):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destination vectors for a Pawn which has not made its opening move.

    Attributes:
        origin: Vector
        offsets: Optional[OpeningVectorSet]
        targeting_computer: Optional[DestinationSpanComputer]
            
    Provides:

    Super Class:
        PawnManeuverVectorBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            offsets: Optional[OpeningManeuverOffsetPattern] |
                              None = OpeningManeuverOffsetPattern(),
            targeting_computer: Optional[VectorTargetingComputer] |
                                None = VectorTargetingComputer(),
    ):
        """
        Args:
            origin: Vector
            offsets: Optional[OpeningVectorSet]
            targeting_computer: Optional[DestinationSpanComputer]
        """
        super().__init__(
            origin=origin,
            offsets=offsets,
            targeting_computer=targeting_computer,
        )

