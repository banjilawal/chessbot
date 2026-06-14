# src/event/maneuver/event.py

"""
Module: event.maneuver.event
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations
from dataclasses import dataclass

from event import Event
from model import Square, Token


@dataclass
class ManeuverEvent(Event):
    traveller: Token
    departure_point: Square
    arrival_point: Square
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, ManeuverEvent):
            return (
                    super().__eq__(other) and
                    self.traveller == other.traveller and
                    self.departure_point == other.departure_point and
                    self.arrival_point == other.arrival_point
            )
        return False
    