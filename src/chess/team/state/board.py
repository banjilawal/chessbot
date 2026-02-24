# src/chess/team/state/board.py

"""
Module: chess.team.state.board
Author: Banji Lawal
Created: 2026-02-24
version: 1.0.0
"""

from __future__ import annotations
from enum import Enum, auto


class TeamBoardState(Enum):
    PARTIALLY_DEPLOYED = auto(),
    WAITING_FOR_DEPLOYMENT = auto(),
    FULLY_DEPLOYED_ON_BOARD = auto(),