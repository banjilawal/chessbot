# src/chess/team/state.py

"""
Module: chess.team.state
Author: Banji Lawal
Created: 2026-02-24
version: 1.0.0
"""

from __future__ import annotations

from enum import Enum, auto


class TeamState(Enum):
    NOT_READY_TO_PLAY = auto(),
    WAITING_TO_PLAY = auto(),
    READY_TO_PLAY = auto(),