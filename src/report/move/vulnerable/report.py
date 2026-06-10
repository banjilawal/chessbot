# src/report/move/vulnerable/report.py

"""
Module: report.move.vulnerable.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from model import Square, Team, Token
from report import MoveOrder


@dataclass
class DestinationVulnerabilityReport(MoveOrder):
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
        MoveOrder
    """
    origin: Square
    recipient: Token
    vulnerable_square: Square
    attacker: Token
    attacker_source: Square
    weight: Optional[int]
    
    @property
    def enemy_team(self) -> Team:
        return self.attacker.team
        
    @property
    def recipient_team(self) -> Team:
        return self.recipient.team
