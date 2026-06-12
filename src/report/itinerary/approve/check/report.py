# src/report/itinerary/approve/check/report.py

"""
Module: report.itinerary.approve.check.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from model import KingToken, Square, Team, Token
from report import ItineraryApprovalReport


@dataclass
class EnemyKingAttackItineraryApproval(ItineraryApprovalReport):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Details a token needs to check an  enemy king.
        
    Attributes:
        origin: Square
        recipient: Token
        target_square: Square
        enemy_king: KingToken
        priority: int
        
        targeted_team: Team
        attacking_team: Team
        
    Provides:

    Super Class:
        Report
    """
    origin: Square
    recipient: Token
    target_square: Square
    enemy_king: KingToken
    priority: Optional[int] = None
    
    @property
    def targeted_team(self) -> Team:
        return self.enemy_king.team
    
    @property
    def attacking_team(self) -> Team:
        return self.recipient.team
