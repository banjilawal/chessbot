# src/report/itinerary/approve/attack/report.py

"""
Module: report.itinerary.approve.attack.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

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
        origin: Square
        recipient: Token
        target_square: Square
        enemy_combatant: CombatantToken
        priority: int
        
        targeted_tem: Team
        attacking_team: Team
        
    Provides:

    Super Class:
        Report
    """
    origin: Square
    recipient: Token
    target_square: Square
    enemy_combatant: CombatantToken
    priority: int
    
    @property
    def targeted_team(self) -> Team:
        return self.enemy_combatant.team
    
    @property
    def attacking_team(self) -> Team:
        return self.recipient.team
