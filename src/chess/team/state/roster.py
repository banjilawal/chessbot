# src/chess/team/state/roster.py

"""
Module: chess.team.state.roster
Author: Banji Lawal
Created: 2026-02-24
version: 1.0.0
"""

from __future__ import annotations
from enum import Enum, auto


class TeamRosterState(Enum):
    ROSTER_EMPTY = auto(),
    ROSTER_FULL = auto(),
    ROSTER_PARTIALLY_FULL = auto(),