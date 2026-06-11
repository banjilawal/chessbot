# src/report/itinerary/approve/peace/report.py

"""
Module: report.itinerary.approve.peace.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from model import CombatantToken, Square, Token
from report import ItineraryApprovalReport


@dataclass
class PeaceItineraryApproval(ItineraryApprovalReport):
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
