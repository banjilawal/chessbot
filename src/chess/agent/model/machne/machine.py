## src/chess/model/machine/machine.py

"""
Module: chess.model.machine.machine
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""
from lib2to3.fixes.fix_import import traverse_imports

from chess.agent import Agent, TeamStackService
from chess.engine.service import EngineService
from chess.team import UniqueTeamDataService


class MachineAgent(Agent):
    _engine_service: EngineService
    
    def __init__(
            self,
            id: int,
            name: str,
            games: UniqueGameDataService = UniqueGameDataService(),
            team_assignments: UniqueTeamDataService = UniqueTeamDataService(),
            engine_service: EngineService = EngineService(),
    ):
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
