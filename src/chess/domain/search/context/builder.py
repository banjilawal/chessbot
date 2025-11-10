# src/chess/domain/search/context/builder.py

"""
Module: chess.domain.search.context.builder
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Optional

from chess.rank import RankBoundsChecker
from chess.coord import Coord, CoordValidator
from chess.system import Builder, BuildResult, IdValidator, LoggingLevelRouter, NameValidator
from chess.domain import (
    VisitorSearchContext, TooManyVisitorSearchParamsException, NoVisitorSearchParamException
)


class VisitorSearchContextBuilder(Builder[VisitorSearchContext]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            visitor_id: Optional[int] = None,
            visitor_name: Optional[str] = None,
            visitor_ransom: Optional[int] = None,
            visitor_coord: Optional[Coord] = None,
            visitor_rank: Optional[str] = None,
            visitor_team_id: Optional[id] = None,
            visitor_team: Optional[str] = None
    ) -> BuildResult[VisitorSearchContext]:
        """"""
        method = "VisitorSearchContextBuilder.build"
        
        try:
            params = [
                visitor_name, visitor_ransom, visitor_id, visitor_team_id, visitor_team, visitor_rank, visitor_coord
            ]
            param_count = sum(bool(p) for p in params)
            
            if param_count == 0:
                return BuildResult.failure(
                    NoVisitorSearchParamException(f"{method}: {NoVisitorSearchParamException.DEFAULT_MESSAGE}")
                )
            
            if param_count > 1:
                return BuildResult.failure(
                    TooManyVisitorSearchParamsException(
                        f"{method}: {TooManyVisitorSearchParamsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if visitor_id is not None:
                id_validation = IdValidator.validate(visitor_id)
                if not id_validation.is_failure():
                    return BuildResult.result(id_validation.exception)
            
            if visitor_name is not None:
                name_validation = NameValidator.validate(visitor_name)
                if name_validation.is_failure():
                    return BuildResult.failure(name_validation.exception)
            
            if visitor_team_id is not None:
                team_id_validation = IdValidator.validate(visitor_team_id)
                if team_id_validation.is_failure():
                    return BuildResult.failure(team_id_validation.exception)
            
            if visitor_team is not None:
                team_name_validation = NameValidator.validate(visitor_team)
                if team_name_validation.is_failure():
                    return BuildResult.failure(team_name_validation.exception)
            
            if visitor_rank is not None:
                rank_name_bounds = RankBoundsChecker.name_bounds_check(visitor_rank.upper())
                if rank_name_bounds.is_failure():
                    return BuildResult.failure(rank_name_bounds.exception)
            
            if visitor_ransom is not None:
                ransom_bounds_check = RankBoundsChecker.ransom_bounds_check(visitor_ransom)
                if ransom_bounds_check.is_failure():
                    return BuildResult.failure(ransom_bounds_check.exception)
            
            if visitor_coord is not None:
                coord_validation = CoordValidator.validate(visitor_coord)
                if coord_validation.is_failure():
                    return BuildResult.failure(coord_validation.exception)
            
            return BuildResult.success(
                VisitorSearchContext(
                    visitor_id=visitor_id,
                    visitor_name=visitor_name,
                    visitor_coord=visitor_coord,
                    visitor_ransom=visitor_ransom,
                    visitor_team_id=visitor_team_id,
                    visitor_team=visitor_team,
                    visitor_rank=visitor_rank
                )
            )
        except Exception as e:
            return BuildResult.failure(e)
