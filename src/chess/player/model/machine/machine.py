# src/chess/player/model/machine/machine.py

"""
Module: chess.player.model.machine.machine
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.player import Player
from chess.engine import EngineService
from chess.team import UniqueTeamDataService


class MachinePlayer(Player):
    """
    # ROLE: Controller

    # RESPONSIBILITIES:
    1.  Forward requests and commands from a Machine player to the Game model.

    # PARENT:
        *   Player

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   engine_service (EngineService)
    
    # INHERITED ATTRIBUTES:
        *   See Player class for inherited attributes.
    """
    _engine_service: EngineService
    
    def machine(
            self,
            id: int,
            name: str,
            engine_service: EngineService = EngineService(),
            teams: UniqueTeamDataService = UniqueTeamDataService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   games (UniqueGameDataService)
            *   teams (UniqueTeamDataService)
            *   engine_service (EngineService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, teams=teams)
        self._engine_service = engine_service
    
    @property
    def engine_service(self) -> EngineService:
        return self._engine_service
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, MachinePlayer): return True
        return False
    
    def __hash__(self):
        return super.__hash__()
