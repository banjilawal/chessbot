# src/sync/turn/referee/turn.py

"""
Module: sync.turn.referee.turn
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from artifcat import TurnResult
from domain import PlayerArchetypeBinder
from util import LoggingLevelRouter


class TurnReferee:
    
    def __init__(self,):
        """
        Args:
        """
        
    @property
    def players(self) -> PlayerArchetypeBinder:
        return self._players
    
    @LoggingLevelRouter.monitor
    def execute(self, players: PlayerArchetypeBinder) -> TurnResult:
        pass
        
    