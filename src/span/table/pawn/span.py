# src/span/table/pawn/span.py

"""
Module: span.table.pawn.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict

from container import VectorSet
from model import Vector


class PawnVectorSetTable:
    """
    Role:
        -   Computation Worker
        -   Integrity Management

    Responsibilities:
        1.  Prevent ArrayIndexOutOfMovement errors by calculating the last point in the direction
            of travel

    Attributes:
        opening_maneuver: VectorSet
        developed_maneuver: VectorSet
        opening_attack: VectorSet
        developed_attack: VectorSet
        
    Provides:

    Super Class:
    """
    _entries: Dict[str: VectorSet]
    
    _opening_maneuver = VectorSet((Vector(x=0, y=1), Vector(x=0, y=2)))
    _developed_maneuver = VectorSet((Vector(x=0, y=1),))
    _opening_attack = VectorSet(
        (
            Vector(x=0, y=1), Vector(x=-1, y=1), Vector(x=1, y=1),
            Vector(x=0, y=2),Vector(x=-1, y=2), Vector(x=1, y=2),
        )
    )
    _developed_attack = VectorSet(
        (
            Vector(x=0, y=1), Vector(x=-1, y=1), Vector(x=1, y=1),
        )
    )
    
    def __init__(self):
        """
        """
        self._entries = {
            "opening_maneuver": self._opening_maneuver,
            "developed_maneuver": self._developed_maneuver,
            "opening_attack": self._opening_attack,
            "developed_attack": self._developed_attack,
        }
    
    @property
    def opening_maneuver(self) -> VectorSet:
        return self._entries["opening_maneuver"]
    
    @property
    def developed_maneuver(self) -> VectorSet:
        return self._entries["developed_maneuver"]
    
    @property
    def opening_attack(self) -> VectorSet:
        return self._entries["opening_attack"]
    
    @property
    def developed_attack(self) -> VectorSet:
        return self._entries["developed_attack"]
