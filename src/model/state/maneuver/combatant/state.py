# src/model/state/maneuver/state.py

"""
Module: model.state.maneuver.state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from enum import Enum, auto


class CombatantManeuverWarning(Enum):
    VULNERABLE_DESTINATION = auto(),
    DESTINATION_IS_SAFE = auto(),