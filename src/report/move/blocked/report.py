# src/report/move/blocked/report.py

"""
Module: report.move.blocked.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from model import CombatantToken, Square, Token
from report import MoveOrder


@dataclass
class MoveBlockerReport(MoveOrder):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Provide information about a move that was blocked by a friendly.
        
    Attributes:
        origin: Square
        recipient: Token
        destination: Square
        enemy: CombatantToken
        priority: int
        
    Provides:

    Super Class:
        Report
    """
    origin: Square
    recipient: Token
    blocked_square: Square
    friendly: Token
    team: Team
