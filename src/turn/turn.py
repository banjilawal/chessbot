# src/turn/__init__.py

"""
Module: turn.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Player
from result import TurnResult
from util import LoggingLevelRouter


class Turn:
    _player: Player
    
    @LoggingLevelRouter.monitor
    def execute_move(self) -> TurnResult:
        return self._player.execute_move(approval: ApprovalReport)
    