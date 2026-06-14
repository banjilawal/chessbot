# src/report/itinerary/occupation/report.py

"""
Module: report.itinerary.occupation.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass


from report import ItineraryReport
from model import Square, Token


@dataclass
class ItineraryApprovalReport(ABC, ItineraryReport):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Details a token needs to visit a Square.
        
    Attributes:
        id: int
        origin: Square
        recipient: Token
        destination: Square
        
    Provides:

    Super Class:
        Report
    """
    destination: Square
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ItineraryApprovalReport):
            return super().__eq__(other)
        return False
