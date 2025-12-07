# src/chess/rank/searcher/service.py

"""
Module: chess.rank.searcher.searcher
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""
from typing import List


from chess.system import LoggingLevelRouter, SearchResult
from chess.rank import RankSpec, RankSearchException


class RankSearch:
    """"""

    @classmethod
    @LoggingLevelRouter.monitor
    def by_id(cls, id: int) -> SearchResult[List[RankSpec]]:
        """"""
        method = "RankSearch.by_id"
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
        method = "RankSearch.by_name"
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
        method = "RankSearch.by_ransom"
        matches = [spec for spec in RankSpec if spec.ransom == ransom]
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.success(payload=matches)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def by_team_quota(cls, team_quota: int) -> SearchResult[List[RankSpec]]:
        """"""
        method = "RankSearch.by_team_quota"
        matches = [spec for spec in RankSpec if spec.team_quota == team_quota]
        if len(matches) == 0:
            return SearchResult.empty()
        return SearchResult.success(payload=matches)
        
    @classmethod
    @LoggingLevelRouter.monitor
    def by_designation(cls, designation: str) -> SearchResult[List[RankSpec]]:
        """"""
        method = "RankSearch.by_designation"
        matches = [spec for spec in RankSpec if spec.designation.upper() == designation.upper()]
        if len(matches) == 0:
            return SearchResult.empty()
        if len(matches) == 1:
            return SearchResult.success(payload=matches)
        if len(matches) > 1:
            return SearchResult.failure(
                RankSearchException(f"{method}: {RankSearchException.DEFAULT_MESSAGE}")
            )