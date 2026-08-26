# src/artifact/report/itinerary/occupation/report.py

"""
Module: artfifact.report.itinerary.occupation.report
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass


from artifcat.report import ItineraryReport


@dataclass
class ItineraryDenialReport(ItineraryReport):
    """
    Role:
        -  Test results

    Responsibilities:
        1.  Details about why a token was denied permission to occupy a square.
        
    Attributes:
        id: int
        origin: Square
        recipient: Token
        
    Provides:

    Super Class:
        ItineraryReport
    """
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ItineraryDenialReport):
            return super().__eq__(other)
        return False
