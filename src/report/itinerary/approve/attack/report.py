# src/report/itinerary/approve/attack/report.py

"""
Module: report.itinerary.approve.attack.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from model import CombatantToken, Square, Team, Token
from report import ItineraryApprovalReport


@dataclass
class AttackItineraryApproval(ItineraryApprovalReport):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Details a token needs to capture an enemy combatant.
        
    Attributes:
        id: int
        origin: Square
        recipient: Token
        target_square: Square
        enemy_combatant: CombatantToken
        priority: int
        
        targeted_team: Team
        attacking_team: Team
        
    Provides:

    Super Class:
        Report
    """
    target_square: Square
    enemy_combatant: CombatantToken
    priority: Optional[int] = None
    
    @property
    def targeted_team(self) -> Team:
        return self.enemy_combatant.team
    
    @property
    def attacking_team(self) -> Team:
        return self.recipient.team
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AttackItineraryApproval):
            return (
                super().__eq__(other) and
                self.priority == other.priority and
                self.target_square == other.target_square and
                self.enemy_combatant == other.enemy_combatant
            )
        return False
