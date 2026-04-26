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
from system import LoggingLevelRouter
from model import Team, TeamBlueprint

class TeamAssembler(Assembler[Team]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, blueprint: TeamBlueprint,) -> BuildResult[Team]:
        """
       .Assembly.he appropriate Team.

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
        
        
