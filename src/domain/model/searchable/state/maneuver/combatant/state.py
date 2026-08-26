# src/domain/model/state/maneuver/state.py

"""
Module: domain.model.searchable.state.maneuver.state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto


class CombatantManeuverWarning(Enum):
    VULNERABLE_DESTINATION = auto(),
    DESTINATION_IS_SAFE = auto(),