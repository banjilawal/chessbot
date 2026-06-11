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
class BlockedItinerary(ItineraryDenialReport):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Provide details about a itinerary that was blocked by a friendly already in the destination.
        
    Attributes:
        origin: Square
        recipient: Token
        blocked_destination: Square
        friendly: Token
        
    Provides:

    Super Class:
        ItineraryDenialReport
    """
    origin: Square
    recipient: Token
    blocked_destination: Square
    friendly: Token
    
    @property
    def team(self) -> Team:
        return self.recipient.team
