# src/chess/battle_space/service.py

"""
Module: chess.battle_space.search
Author: Banji Lawal
Created: 2025-10-27
version: 1.0.0
"""
from chess.battle_space import Projection, ProjectionSearchContext, WhiteTeamProjectionSearch
from chess.battle_space.service import ProjectionService
from chess.system import LoggingLevelRouter, SearchResult
from chess.team import TeamSchema


class ProjectionSearch:
    
    @classmethod
    @LoggingLevelRouter.monitor
    def search(
            cls,
            schema: TeamSchema,
            data_owner: ProjectionService,
            search_context: ProjectionSearchContext
    ) -> SearchResult[Projection]:
        
        if schema == TeamSchema.WHITE:
            return WhiteTeamProjectionSearch.search(data_owner, search_context)