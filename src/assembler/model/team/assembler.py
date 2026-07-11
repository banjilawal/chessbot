# src/assembler/model/team/py

"""
Module: assembler.model.team.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from result import BuildResult
from util import LoggingLevelRouter
from model import Team, TeamBlueprint
from controller import WorkerRegistryController

class TeamAssembler(Assembler[Team]):
    NAME = "team_assembler"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, blueprint: TeamBlueprint,) -> BuildResult[Team]:
        """
        Assemble the appropriate Team.

        Args:
            blueprint: TeamBlueprint
        Returns:
            BuildResult[Team]
        Raises:
        """
        method = f"{cls.__name__}.execute"
        return BuildResult.success(
            Team(
                id=blueprint.id,
                board=blueprint.board,
                owner=blueprint.model_class,
                schema=blueprint.schema,
            )
        )

# Register the 
WorkerRegistryController.register_worker(worker=TeamAssembler)
        
