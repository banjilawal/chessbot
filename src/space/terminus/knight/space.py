# src/space/terminus/knight/space.py

"""
Module: space.terminus.knight.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Tuple

from model import Vector


class KnightTerminusList:
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
    _entries: Tuple[Vector, ...]
    
    def __init__(self):
        _entries = (
            Vector(1, 2), Vector(-1, 2), Vector(1, -2), Vector(-1, -2),
            Vector(2, 1), Vector(2, -1), Vector(-2, 1), Vector(-2, -1),
        )
        
    @property
    def termini(self) -> Tuple[Vector, ...]:
        return self._entries