# src/chess/domain/searcher/factory.py

"""
Module: chess.domain.searcher.builder
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Optional

from chess.rank import RankBoundsChecker
from chess.coord import Coord, CoordValidator
from chess.system import Builder, BuildResult, IdValidator, LoggingLevelRouter, NameValidator
from chess.domain import (
    VisitorSearchContext, ExcessiveVisitorSearchParamsException, NoVisitorSearchFilterSelectionException
)


class VisitorSearchContextBuilder(Builder[VisitorSearchContext]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            id: Optional[int] = None,
            name: Optional[str] = None,
            ransom: Optional[int] = None,
            coord: Optional[Coord] = None,
            rank_name: Optional[str] = None,
            team_id: Optional[id] = None,
            team_name: Optional[str] = None
    ) -> BuildResult[VisitorSearchContext]:
        """"""
        method = "VisitorSearchContextBuilder.builder"
        
        try:
            params = [name, ransom, id, team_id, team_name, rank_name, coord]
            param_count = sum(bool(p) for p in params)
            
            if param_count == 0:
                return BuildResult.failure(
                    NoVisitorSearchFilterSelectionException(
                        f"{method}: {NoVisitorSearchFilterSelectionException.DEFAULT_MESSAGE}"
                    )
                )
            
            if param_count > 1:
                return BuildResult.failure(
                    ExcessiveVisitorSearchParamsException(
                        f"{method}: {ExcessiveVisitorSearchParamsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if id is not None:
                id_validation = IdValidator.validate(id)
                if not id_validation.is_failure():
                    return BuildResult.result(id_validation.exception)
            
            if name is not None:
                name_validation = NameValidator.validate(name)
                if name_validation.is_failure():
                    return BuildResult.failure(name_validation.exception)
            
            if team_id is not None:
                team_id_validation = IdValidator.validate(team_id)
                if team_id_validation.is_failure():
                    return BuildResult.failure(team_id_validation.exception)
            
            if team_name is not None:
                team_name_validation = NameValidator.validate(team_name)
                if team_name_validation.is_failure():
                    return BuildResult.failure(team_name_validation.exception)
            
            if rank_name is not None:
                rank_name_bounds = RankBoundsChecker.name_bounds_check(rank_name.upper())
                if rank_name_bounds.is_failure():
                    return BuildResult.failure(rank_name_bounds.exception)
            
            if ransom is not None:
                ransom_bounds_check = RankBoundsChecker.ransom_bounds_check(ransom)
                if ransom_bounds_check.is_failure():
                    return BuildResult.failure(ransom_bounds_check.exception)
            
            if coord is not None:
                coord_validation = CoordValidator.validate(coord)
                if coord_validation.is_failure():
                    return BuildResult.failure(coord_validation.exception)
            
            return BuildResult.success(
                VisitorSearchContext(
                    visitor_id=id,
                    visitor_name=name,
                    visitor_coord=coord,
                    visitor_ransom=ransom,
                    visitor_team_id=team_id,
                    visitor_name=team_name,
                    visitor_rank=rank_name
                )
            )
        except Exception as e:
            return BuildResult.failure(e)
