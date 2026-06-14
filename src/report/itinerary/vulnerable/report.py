# src/report/itinerary/vulnerable/report.py

"""
Module: report.itinerary.vulnerable.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from model import Square, Team, Token
from report import ItineraryReport


@dataclass
class ItineraryVulnerabilityReport(ItineraryReport):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Provide details about a destination the enemy can attack.
        
    Attributes:
        origin: Square
        recipient: KingToken
        vulnerable_square: Square
        attacker: Token
        attacker_source: Square
        weight: Optional[int]
        
    Provides:

    Super Class:
        ItineraryOrder
    """
    attacker: Token
    attacker_source: Square
    vulnerable_square: Square
    weight: Optional[int]
    
    @property
    def enemy_team(self) -> Team:
        return self.attacker.team
        
    @property
    def recipient_team(self) -> Team:
        return self.recipient.team
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ItineraryVulnerabilityReport):
            return (
                    super().__eq__(other) and
                    self.attacker == other.attacker and
                    self.attacker_source == other.attacker_source and
                    self.vulnerable_square == other.vulnerable_square and
                    self.weight == other.weight
            )
        return False
