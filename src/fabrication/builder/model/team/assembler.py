# src/fabrication/builder/model/team/fabrication/builder.py

"""
Module: fabrication.builder.model.team.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from fabrication.builder import ModelBuilder
from domain.metadata.blueprint import TeamBlueprint
from domain.model import Team
from artifcat import BuildResult
from util import LoggingLevelRouter


class TeamBuilder(ModelBuilder[Team]):
    
    
    @LoggingLevelRouter.monitor
    def execute(self, request: TeamBlueprint, ) -> BuildResult[Team]:
        """
        Assemble a Team from the Blueprint's contents.

        Args:
            request: TeamBlueprint
        Returns:
            BuildResult[Team]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        return BuildResult.success(
            Team(
                id=request.id,
                board=request.board,
                owner=request.owner,
                archetype=request.archetype,
            )
        )

        
