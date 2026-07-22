# src/assembler/model/team/assembler.py

"""
Module: assembler.model.team.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from assembler import ModelAssembler
from blueprint import TeamBlueprint
from model import Team
from result import BuildResult
from util import LoggingLevelRouter


class TeamAssembler(ModelAssembler[Team]):
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: TeamBlueprint,) -> BuildResult[Team]:
        """
        Assemble a Team from the Blueprint's contents.

        Args:
            blueprint: TeamBlueprint
        Returns:
            BuildResult[Team]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        return BuildResult.success(
            Team(
                id=blueprint.id,
                board=blueprint.board,
                owner=blueprint.owner,
                archetype=blueprint.archetype,
            )
        )

        
