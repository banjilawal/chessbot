# src/game/turn/adviser/game.py

"""
Module: game.turn.adviser.game
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from artifcat import AuthorizationDecision
from graph import Graph
from util import LoggingLevelRouter


class TurnAdviser:
    
    
    @LoggingLevelRouter.monitor
    def advice(self, graph: Graph) -> AuthorizationDecision:
        pass