# src/game/encounter/report.py

"""
Module: game.encounter.report
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict

from collection import CheckChain
from config import GameColor
from domain import Arena, CheckmateEncounter, Player, Team


class Checkmate:
    """
    Role:
        - Reporting

    Responsibilities:
        1.  Details about  the encounter and their encounter moves.
        
    Attributes:
        encounter: Encounter
        mmoves: CheckChain
        encounter_has_right_team: bool
        encounter_has_wrong_team: bool
        
    Provides:

    Super Class:
    """
    _encounter: CheckmateEncounter
    _blocked_routes:  CheckChain
    
    def __init__(self, encounter: CheckmateEncounter, blocked_routes: CheckChain, ):
        """
        Args:
            encounter: CheckmateEncounter
            blocked_routes: CheckChain
        """
        self._encounter = encounter
        self._blocked_routes = blocked_routes
        
    @property
    def encounter(self) -> CheckmateEncounter:
        return self._encounter
    
    @property
    def blocked_routes(self) -> CheckChain:
        return self._blocked_routes
    
    