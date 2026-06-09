# src/report/move/deny/checked/__init__.py

"""
Module: report.move.deny.checked.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from model import KingToken, Square, Team, Token
from report import MoveDenialReport


@dataclass
class DestinationChecked(MoveDenialReport):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Provide details about an enemy who could reach the king if it moved to
            the destination.
        
    Attributes:
        origin: Square
        recipient: KingToken
        checked_square: Square
        check_holder: Token
        
    Provides:

    Super Class:
        MoveDenialReport
    """
    origin: Square
    recipient: KingToken
    checked_square: Square
    check_holder: Token
    
    @property
    def enemy_team(self) -> Team:
        return self.check_holder.team
        
    @property
    def recipient_team(self) -> Team:
        return self.recipient.team
