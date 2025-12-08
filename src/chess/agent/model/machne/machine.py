## src/chess/model/machine/machine.py

"""
Module: chess.model.machine.machine
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import Agent
from chess.engine import EngineService
from chess.game import UniqueGameDataService
from chess.team import UniqueTeamDataService


class MachineAgent(Agent):
    """
    # ROLE: Controller

    # RESPONSIBILITIES:
    1.  Forward requests and commands from a Machine player to the Game model.

    # PARENT
        *   Agent

    # PROVIDES:
    MachineAgent

    # LOCAL ATTRIBUTES:
        *   engine_service (EngineService)
    
    # INHERITED ATTRIBUTES:
    See Agent class for inherited attributes.
    """
    _engine_service: EngineService
    
    def __init__(
            self,
            id: int,
            name: str,
            games: UniqueGameDataService = UniqueGameDataService(),
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

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=name, games=games, team_assignments=team_assignments)
        self._engine_service = engine_service
    
    @property
    def engine_service(self) -> EngineService:
        return self._engine_service
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, MachineAgent): return True
        return False
    
    def __hash__(self):
        return super.__hash__()
