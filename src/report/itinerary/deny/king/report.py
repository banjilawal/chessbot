# src/report/itinerary/deny/checked/report.py

"""
Module: report.itinerary.deny.checked.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from model import KingToken, Square, Team, Token
from report import ItineraryDenialReport


@dataclass
class KingSafetyViolation(ItineraryDenialReport):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Provide details an itinerary that was denied because it would put a King in in check.
        
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
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, KingSafetyViolation):
            return (
                    super().__eq__(other) and
                    self.check_holder == other.check_holder and
                    self.enemy_source == other.enemy_source and
                    self.checked_square == other.checked_square
            )
        return False

