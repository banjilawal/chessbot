# src/report/itinerary/approve/maneuver/report.py

"""
Module: report.itinerary.approve.maneuver.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from model import CombatantToken, Square, Token
from report import ItineraryApprovalReport


@dataclass
class ManeuverApproval(ItineraryApprovalReport):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Details an empty square a token can occupy.
        
    Attributes:
        id: int
        origin: Square
        recipient: Token
        destination: Square
        cost: Optional[int]
        
    Provides:

    Super Class:
        Report
    """
    destination: Square
    cost: Optional[int] = None
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ManeuverApproval):
            return (
                    super().__eq__(other) and
                    self.cost == other.cost and
                    self.destination == other.destination
            )
        return False
