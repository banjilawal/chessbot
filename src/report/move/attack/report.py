# src/report/move/attack/report.py

"""
Module: report.move.attack.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from model import CombatantToken, Square, Token
from report import MoveOrder


@dataclass
class AttackOrder(MoveOrder):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Details a token needs to capture an enemy.
        
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
    destination: Square
    enemy: CombatantToken
    priority: int
