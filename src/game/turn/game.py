# src/game/turn/game.py

"""
Module: game.turn.game
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat import TurnResult
from domain import Graph, Player
from operation.microservice.maneuver import ManeuverLauncher
from util import LoggingLevelRouter


class Turn:
    _id: int
    _player: Player
    _graph: Graph
    _maneuver_launcher: ManeuverLauncher
    
    def game(
            self,
            id: int,
            graph: Graph,
            player: Player,
            maneuver_launcher: Optional[ManeuverLauncher] | None = None,
    ):
        """
        Args:
            id: int
            graph: Graph
            player: Player
            maneuver_launcher: ManeuverLauncher
        """
        self.id = id
        self._player = player
        self._graph = graph
        self._maneuver_launcher = maneuver_launcher or ManeuverLauncher()
    
    @LoggingLevelRouter.monitor
    def execute(self, ) -> TurnResult:
        
        approval = self._player.adviser.advice(graph=self._graph)
        return self._maneuver_launcher.execute(approval)
    