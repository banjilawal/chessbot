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
    