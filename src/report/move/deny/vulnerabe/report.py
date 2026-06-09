# src/report/move/deny/vulnerable/__init__.py

"""
Module: report.move.deny.vulnerable.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from model import CombatantToken, KingToken, Square, Team, Token
from report import MoveDenialReport


@dataclass
class DestinationVulnerable(MoveDenialReport):
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
        MoveDenialReport
    """
    origin: Square
    recipient: CombatantToken
    vulnerable_square: Square
    attacker: Token
    attacker_source: Square
    weight: Optional[int]
    
    @property
    def enemy_team(self) -> Team:
        return self.check_holder.team
        
    @property
    def recipient_team(self) -> Team:
        return self.recipient.team
