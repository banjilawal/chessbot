# src/chess/agent/agent/machine.py

"""
Module: chess.agent.machine
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import PlayerAgent, TeamStackService
from chess.engine.service import EngineService


class MachinePlayer(PlayerAgent):
    _engine_service: EngineService
    
    def __init__(
            self,
            id: int,
            name: str,
            team_stack_service: TeamStackService = TeamStackService(),
            engine_service: EngineService = EngineService(),
    ):
        super().__init__(id=id, name=name, team_stack_service=team_stack_service)
        self._engine_service = engine_service
    
    @property
    def engine_service(self) -> EngineService:
        return self._engine_service
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, MachinePlayer):
                return True
        return False
    
    def __hash__(self):
        return super.__hash__()
    
    def __str__(self):
        return f"{super().__str__()} engine:{self._engine.__class__.__name__.title()}"
