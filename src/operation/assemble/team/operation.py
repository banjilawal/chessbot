# src/operation/assemble/team/operation.py

"""
Module: operation.assemble.team.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from operation import Assembler
from result import BuildResult
from system import  LoggingLevelRouter
from model import Board, Team, TeamBlueprint

class TeamAssembler(Assembler[Team]):
    
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
        
        
