# src/artifact/report/collision/state.py

"""
Module: artfifact.report.collision.state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from enum import Enum, auto


class CollisionState(Enum):
    NO_COLLISIONS = auto(),
    COLLISION_DETECTED = auto(),