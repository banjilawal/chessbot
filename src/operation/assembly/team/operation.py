# src/operation/assembly/team/operation.py

"""
Module: operation.assembly.team.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from result import BuildResult
from operation import Assembler
from util import LoggingLevelRouter
from model import Team, TeamBlueprint
from controller import WorkerRegistryController

class TeamAssembler(Assembler[Team]):
    OPERATION_NAME = "team_assembler"
    
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
                owner=blueprint.owner,
                schema=blueprint.schema,
            )
        )

# Register the operation.
WorkerRegistryController.register(worker=TeamAssembler)
        
