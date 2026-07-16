# src/span/table/knight/span.py

"""
Module: span.table.knight.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict

from container import VectorSet
from model import Vector


class VectorSetGroupTable:
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
    _king_vectors = VectorSet(
        (
            Vector(1, 0), Vector(-1, 0), Vector(0, 1),
            Vector(1, 1), Vector(-1, 1), Vector(-1, -1), Vector(1, -1)
        )
    )
    _knight_vectors: VectorSet = VectorSet(
        (
            Vector(1, 2), Vector(-1, 2), Vector(1, -2), Vector(-1, -2),
            Vector(2, 1), Vector(2, -1), Vector(-2, 1), Vector(-2, -1),
        )
    )
    
    @property
    def knight_movement_vectors(self) -> VectorSet:
        return self._knight_vectors
    
    @property
    def king_movement_vectors(self) -> VectorSet:
        return self._king_vectors
