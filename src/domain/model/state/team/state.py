# src/dossier/model/state/team/state.py

"""
Module: domain.model.state.team.state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto


class TeamState(Enum):
    NOT_READY_TO_PLAY = auto(),
    WAITING_TO_PLAY = auto(),
    READY_TO_PLAY = auto(),