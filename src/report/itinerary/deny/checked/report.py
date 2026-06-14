# src/report/itinerary/deny/checked/__init__.py

"""
Module: report.itinerary.deny.checked.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from model import KingToken, Square, Team, Token
from report import ItineraryDenialReport


@dataclass
class KingItineraryChecked(ItineraryDenialReport):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Provide details about an enemy who could reach the king if it itineraryd to
            the destination.
        
    Attributes:
        id: int
        recipient: KingToken
        checked_square: Square
        check_holder: Token
        
        enemy_team: Team
        recipient_team: Team
        
    Provides:

    Super Class:
        ItineraryDenialReport
    """
    recipient: KingToken
    checked_square: Square
    check_holder: Token
    enemy_source: Square
    
    @property
    def enemy_team(self) -> Team:
        return self.check_holder.team
        
    @property
    def recipient_team(self) -> Team:
        return self.recipient.team
