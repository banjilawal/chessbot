# src/schema/orientation/quadrant/schema.py

"""
Module: schema.orientation.quadrant.schema
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from enum import Enum, auto


class QuadrantOrientation(Enum):
    NORTHEAST = auto(),
    NORTHWEST = auto(),
    SOUTHEAST = auto(),
    SOUTHWEST = auto(),

