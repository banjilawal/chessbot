# src/report/itinerary/deny/blocked/report.py

"""
Module: report.itinerary.deny.blocked.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from model import Square, Team, Token
from report import ItineraryDenialReport


@dataclass
class BlockingReport(ItineraryDenialReport):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Provide details about a itinerary that was blocked by a friendly already in the destination.
        
    Attributes:
        id: int
        origin: Square
        recipient: Token
        blocked_destination: Square
        friendly: Token
        
    Provides:

    Super Class:
        ItineraryDenialReport
    """
    blocked_destination: Square
    friendly: Token
    
    @property
    def team(self) -> Team:
        return self.recipient.team
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, BlockingReport):
            return (
                    super().__eq__(other) and
                    self.friendly == other.friendly and
                    self.blocked_destination == other.blocked_destination
            )
        return False
