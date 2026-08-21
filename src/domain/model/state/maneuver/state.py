# src/dossier/model/state/maneuver/state.py

"""
Module: domain.model.state.maneuver.state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto


class ManeuverState(Enum):
    COMPLETED = auto(),
    NOT_COMPLETED = auto(),