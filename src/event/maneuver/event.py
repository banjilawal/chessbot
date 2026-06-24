# src/event/maneuver/event.py

"""
Module: event.maneuver.event
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from event import Event
from model import Square, Token


class ManeuverEvent(Event):
    _traveller: Token
    _departure_point: Square
    _arrival_point: Square
    
    def __init__(
            self,
            id: int,
            traveller: Token,
            departure_point: Square,
            arrival_point: Square,
            parent: Event | None = None,
    ):
        super().__init__(id=id, parent=parent)
        self._traveller = traveller
        self._departure_point = departure_point
        self._arrival_point = arrival_point
        
    @property
    def traveller(self) -> Token:
        return self._traveller
    
    @property
    def departure_point(self) -> Square:
        return self._departure_point
    
    @property
    def arrival_point(self) -> Square:
        return self._arrival_point
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, ManeuverEvent):
            return (
                    super().__eq__(other) and
                    self._traveller == other.traveller and
                    self._arrival_point == other.arrival_point and
                    self._departure_point == other.departure_point
            )
        return False
    