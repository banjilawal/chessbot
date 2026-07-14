# src/geometry/point/cardinal/geometry.py

"""
Module: geometry.point.cardinal.geometry
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from enum import Enum, auto


class CardinalPoint(Enum):
    NORTH = auto(),
    NORTHEAST = auto(),
    SOUTHEAST = auto(),
    SOUTH = auto(),
    SOUTHWEST = auto(),
    WEST = auto(),
    