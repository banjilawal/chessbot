# src/schema/offset/schema.py

"""
Module: schema.offset.schema
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from enum import Enum
from typing import Dict

from container import VectorSet
from model import Vector


class Offset(Enum):
    def __new__(
            cls,
            entries: VectorSet,
    ):
        """
        Args:
            entries: Dict[str: VectorOffset]
        """
        obj = object.__new__(cls)
        obj._entry = VectorSet
        return obj
    
    KNIGHT = (
        VectorSet(
            (
                Vector(1, 2), Vector(-1, 2), Vector(1, -2), Vector(-1, -2),
                Vector(2, 1), Vector(2, -1), Vector(-2, 1), Vector(-2, -1),
            )
        )
    ),
    KING = (
        VectorSet(
            (
                Vector(1, 0), Vector(-1, 0), Vector(0, 1),
                Vector(1, 1), Vector(-1, 1), Vector(-1, -1), Vector(1, -1)
            )
        )
    )
    DEVELOPED_PAWN_MANEUVER = (
        VectorSet(
            (Vector(x=0, y=1),)
        )
    )
    OPENING_PAWN_MANEUVER = (
        VectorSet(
            (Vector(x=0, y=1), Vector(x=0, y=2),)
        )
    )
    DEVELOPED_PAWN_ATTACK = (
        VectorSet(
            (Vector(x=-1, y=1), Vector(x=1, y=1),)
        )
    )
    OPENING_PAWN_ATTACK = (
        VectorSet(
            (
                Vector(x=-1, y=1), Vector(x=1, y=1),
                Vector(x=-1, y=2), Vector(x=1, y=2),
            )
        )
    )

    
    @property
    def entries(self) -> Dict[str: VectorOffset]:
        return self._entry
    

