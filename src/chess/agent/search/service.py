# src/chess/agent/search/service.py

"""
Module: chess.agent.search.service
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""
from typing import List, cast

from chess.agent import (
    Agent, TeamSearch, TeamSearchContext, TeamSearchContextBuilder, TeamSearchContextValidator,
    TeamSearchException
)
from chess.system import SearchResult
from chess.team import Team


class TeamSearchService:
    _search: type[TeamSearch]
    _search_context_builder: type[TeamSearchContextBuilder]
    _search_context_validator: type[TeamSearchContextValidator]

    
    
    def __init__(
            self,
            search: type[TeamSearch] = TeamSearch,
            search_context_builder: type[TeamSearchContextBuilder] = TeamSearchContextBuilder,
            search_context_validator: type[TeamSearchContextValidator] = TeamSearchContextValidator,

    ):
        self._search = search
        self._search_context_builder = search_context_builder
        self._search_context_validator = search_context_validator
        
    
    def search(self, data_owner: Agent, search_context: TeamSearchContext) -> SearchResult[List[Team]]:
        return self._search.search(data_owner=data_owner, search_context=search_context)
        
        
    def search_by_id(self, data_owner: Agent, id: int) -> SearchResult[List[Team]]:
        method = "TeamSearchService.search_by_id"
        try:
            search_context_build = self._search_context_builder.build(id=id)
            if search_context_build.is_failure():
                return SearchResult.failure(search_context_build.exception)
            search_context = cast(TeamSearchContext, search_context_build.payload)
            
            return self._search.search(data_owner=data_owner, search_context=search_context)
        except Exception as ex:
            return SearchResult.failure(
                TeamSearchException(
                    f"{method}: {TeamSearchException.DEFAULT_MESSAGE}",
                    ex
                )
            )
    
    def search_by_name(self, data_owner: Agent, name: str) -> SearchResult[List[Team]]:
        method = "TeamSearchService.search_by_name"
        try:
            search_context_build = self._search_context_builder.build(name=name)
            if search_context_build.is_failure():
                return SearchResult.failure(search_context_build.exception)
            search_context = cast(TeamSearchContext, search_context_build.payload)
            
            return self._search.search(data_owner=data_owner, search_context=search_context)
        except Exception as ex:
            return SearchResult.failure(
                TeamSearchException(
                    f"{method}: {TeamSearchException.DEFAULT_MESSAGE}",
                    ex
                )
            )
    
    def search_by_color(self, data_owner: Agent, color: GameColor) -> SearchResult[List[Team]]:
        method = "TeamSearchService.search_by_color"
        try:
            search_context_build = self._search_context_builder.build(color=color)
            if search_context_build.is_failure():
                return SearchResult.failure(search_context_build.exception)
            search_context = cast(TeamSearchContext, search_context_build.payload)
            
            return self._search.search(data_owner=data_owner, search_context=search_context)
        except Exception as ex:
            return SearchResult.failure(
                TeamSearchException(
                    f"{method}: {TeamSearchException.DEFAULT_MESSAGE}",
                    ex
                )
            )


