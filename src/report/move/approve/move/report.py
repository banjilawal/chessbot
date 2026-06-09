# src/report/move/approve/move/report.py

"""
Module: report.move.approve.move.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from model import CombatantToken, Square, Token
from report import MoveApprovalReport


@dataclass
class MoveApproval(MoveApprovalReport):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Details an empty square a token can occupy.
        
    Attributes:
        origin: Square
        recipient: Token
        destination: Square
        cost: Optional[int]
        
    Provides:

    Super Class:
        Report
    """
    origin: Square
    recipient: Token
    destination: Square
    cost: Optional[int] = None
