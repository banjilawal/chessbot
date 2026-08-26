# src/transit/dispatcher/builder/pattern/pawn/dispatcher/builder/pattern.py

"""
Module: transit.dispatcher.builder.pattern.pawn.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from collection import VectorSet
from domain.schema import Offset
from topology.pattern import ManeuverOffsetPattern


class OpeningManeuverOffsetPattern(ManeuverOffsetPattern):
    """
    Role:
        -   Data Holder
        -   Immutability

    Responsibilities:
        1.  Determine potential destinations from an opening Pawn's current position.

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        ManeuverOffsetPattern
    """
    
    def __init__(self, offsets: VectorSet = Offset.OPENING_PAWN_MANEUVER.entries):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(offsets=offsets)
    
    
