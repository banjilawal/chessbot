# src/chess/rank/search/search.py

"""
Module: chess.rank.search.search
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""
from typing import List

from chess.system import LoggingLevelRouter, Search, SearchException, SearchResult
from chess.rank import Rank, RankSearchContextValidator, RankSearchException, RankService, RankSearchContext, RankSpec


class RankSpecSearch:
    """"""

    @classmethod
    @LoggingLevelRouter.monitor
    def search(
            cls,
            data_owner: RankService,
            collection: List[Rank],
            search_context: RankSearchContext,
            rank_search_context_validator: type[RankSearchContextValidator] = RankSearchContextValidator,
    ) -> SearchResult[List[Rank]]:
        method = "RankSearch.search"
        try:
            context_validation = rank_search_context_validator.validate(search_context)
            if context_validation.is_failure():
                return SearchResult.failure(context_validation.exception)
            
            if search_context.row is not None:
                return cls.search_by_row(collection=collection, row=search_context.row)
            
            if search_context.column is not None:
                return cls.search_by_column(collection=collection, column=search_context.column)
            
            if search_context.rank is not None:
                return cls.search_by_rank(collection=collection, rank=search_context.rank)
            
        except Exception as ex:
            return SearchResult.failure(
                RankSearchException(
                    f"{method}: {RankSearchException.DEFAULT_MESSAGE}"
                )
            )
        
        
    @classmethod
    @LoggingLevelRouter.monitor
    def by_id(cls, id: int) -> SearchResult[List[RankSpec]]:
        """"""
        method = "RankSpecSearch.by_id"
        matches = [spec for spec in RankSpec if spec.id == id]
        if len(matches) == 0:
            return SearchResult.empty()
        if len(matches) == 1:
            return SearchResult.success(payload=matches)
        if len(matches) > 1:
            return SearchResult.failure(
                RankSearchException(f"{method}: {RankSearchException.DEFAULT_MESSAGE}")
            )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def by_name(cls, name: str) -> SearchResult[List[RankSpec]]:
        """"""
        method = "RankSpecSearch.by_name"
        matches = [spec for spec in RankSpec if spec.name.upper() == name.upper()]
        if len(matches) == 0:
            return SearchResult.empty()
        if len(matches) == 1:
            return SearchResult.success(payload=matches)
        if len(matches) > 1:
            return SearchResult.failure(
                RankSearchException(f"{method}: {RankSearchException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def by_ransom(cls, ransom: int) -> SearchResult[List[RankSpec]]:
        """"""
        method = "RankSpecSearch.by_ransom"
        matches = [spec for spec in RankSpec if spec.ransom == ransom]
        if len(matches) == 0:
            return SearchResult.empty()
        if len(matches) == 1:
            return SearchResult.success(payload=matches)
        if len(matches) > 1:
            return SearchResult.failure(
                RankSearchException(f"{method}: {RankSearchException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def by_team_quota(cls, team_quota: int) -> SearchResult[List[RankSpec]]:
        """"""
        method = "RankSpecSearch.by_team_quota"
        matches = [spec for spec in RankSpec if spec.team_quota == team_quota]
        if len(matches) == 0:
            return SearchResult.empty()
        if len(matches) == 1:
            return SearchResult.success(payload=matches)
        if len(matches) > 1:
            return SearchResult.failure(
                RankSearchException(f"{method}: {RankSearchException.DEFAULT_MESSAGE}")
            )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def by_designation(cls, designation: str) -> SearchResult[List[RankSpec]]:
        """"""
        method = "RankSpecSearch.by_designation"
        matches = [spec for spec in RankSpec if spec.designation.upper() == designation.upper()]
        if len(matches) == 0:
            return SearchResult.empty()
        if len(matches) == 1:
            return SearchResult.success(payload=matches)
        if len(matches) > 1:
            return SearchResult.failure(
                RankSearchException(f"{method}: {RankSearchException.DEFAULT_MESSAGE}")
            )