# src/logic/battle_space/validator.py

"""
Module: logic.battle_space.searcher
Author: Banji Lawal
Created: 2025-10-27
version: 1.0.0
"""
from logic.battle_space import Projection, ProjectionSearchContext, WhiteTeamProjectionFinder
from logic.battle_space.service import ProjectionService
from system import LoggingLevelRouter, SearchResult
from logic.team import TeamSchema


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
            return WhiteTeamProjectionFinder.search(data_owner, search_context)