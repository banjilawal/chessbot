# src/domain/schema/orientation/axis/schema.py

"""
Module: domain.schema.orientation.axis.schema
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto


class AxisOrientation(Enum):
    NORTH = auto(),
    SOUTH = auto(),
    EAST = auto(),
    WEST = auto(),