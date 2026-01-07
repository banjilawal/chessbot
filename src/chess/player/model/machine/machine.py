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
            team_assignments: UniqueTeamDataService = UniqueTeamDataService(),
            engine_service: EngineService = EngineService(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   games (UniqueGameDataService)
            *   team_assignments (UniqueTeamDataService)
            *   engine_service (EngineService)

        # RETURNS:
        None

        # RAISES:
        None
        """
        super().machine(id=id, name=name, games=games, team_assignments=team_assignments)
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
