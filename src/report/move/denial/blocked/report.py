# src/report/move/deny/blocked/report.py

"""
Module: report.move.deny.blocked.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from model import Square, Team, Token
from report import MoveDenialReport


@dataclass
class DestinationBlocked(MoveDenialReport):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Provide details about a move that was blocked by a friendly already in the destination.
        
    Attributes:
        origin: Square
        recipient: Token
        blocked_destination: Square
        friendly: Token
        
    Provides:

    Super Class:
        MoveDenialReport
    """
    origin: Square
    recipient: Token
    blocked_destination: Square
    friendly: Token
    
    @property
    def team(self) -> Team:
        return self.recipient.team
