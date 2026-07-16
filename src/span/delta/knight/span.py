# src/span/delta/knight/span.py

"""
Module: span.delta.knight.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Tuple

from model import Knight, Vector
from span import VectorSet


class KnightDeltaVectors(VectorSet[Knight]):
    """
    Role:
        -   Data Holder
        
    Responsibilities:
        1.  Lists a Knight's possible destinations from its current postion.

    Attributes:
        termini: Tuple[Vector, ...]

    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            entries: Tuple[Vector, ...] = (
                    Vector(1, 2), Vector(-1, 2), Vector(1, -2), Vector(-1, -2),
                    Vector(2, 1), Vector(2, -1), Vector(-2, 1), Vector(-2, -1),
            )
    ):
        super().__init__(entries=entries)
