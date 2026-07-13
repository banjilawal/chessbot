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
from turn import TurnAdviser
from util import LoggingLevelRouter


class Turn:
    _id: int
    _player: Player
    _adviser: TurnAdviser
    
    def __init__(self, id: int, player: Player, adviser: TurnAdviser):
        self.id = id
        self._player = player
        self._adviser = adviser
    
    @LoggingLevelRouter.monitor
    def execute(self,) -> TurnResult:
        
        return self._player.execute_move(self._adviser.advice())
    