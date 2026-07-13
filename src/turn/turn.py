# src/turn/__init__.py

"""
Module: turn.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Graph, Player
from operation import ManeuverLauncher
from report import ManeuverApprovalReport
from result import TurnResult
from turn import TurnAdviser
from util import LoggingLevelRouter


class Turn:
    _id: int
    _player: Player
    _graph: Graph
    _maneuver_launcher: ManeuverLauncher
    
    def __init__(
            self,
            id: int,
            player: Player,
            graph: Graph,
            maneuver_launcher: ManeuverLauncher = ManeuverLauncher(),
    ):
        """
        Args:
            id: int
            player: Player
            adviser: TurnAdviser, graph: Graph
        """
        self.id = id
        self._player = player
        self._graph = graph
        self._maneuver_launcher = maneuver_launcher
    
    @LoggingLevelRouter.monitor
    def execute(self, ) -> TurnResult:
        
        approval = self._player.adviser.advice(graph=self._graph)
        return self._maneuver_launcher.execute(approval)
    