# src/logic/points/searcher/factory.py

"""
Module: logic.points.searcher.builder
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from typing import Optional

from logic.rank import RankBoundsChecker
from logic.coord import Coord, CoordValidationProcess
from logic.system import BuildProcess, BuildResult, IdValidationProcess, LoggingLevelRouter, NameValidationProcess
from logic.domain import (
    VisitorSearchContext, ArenaVisitorSearchParamsException, NoVisitorSearchFilterSelectionException
)


class VisitorSearchContextBuildProcess(BuildProcess[VisitorSearchContext]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
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
        method = "VisitorSearchContextBuildProcess.builder"
        
        try:
            params = [name, ransom, id, team_id, team_name, rank_name, coord]
            param_count = sum(bool(p) for p in params)
            
            if param_count == 0:
                return BuildResult.failure(
                    NoVisitorSearchFilterSelectionException(
                        f"{method}: {NoVisitorSearchFilterSelectionException.MSG}"
                    )
                )
            
            if param_count > 1:
                return BuildResult.failure(
                    ArenaVisitorSearchParamsException(
                        f"{method}: {ArenaVisitorSearchParamsException.MSG}"
                    )
                )
            
            if id is not None:
                id_validation = IdValidationProcess.execute(id)
                if not id_validation.is_failure():
                    return BuildResult.result(id_validation.exception)
            
            if name is not None:
                name_validation = NameValidationProcess.execute(name)
                if name_validation.is_failure():
                    return BuildResult.failure(name_validation.exception)
            
            if team_id is not None:
                team_id_validation = IdValidationProcess.execute(team_id)
                if team_id_validation.is_failure():
                    return BuildResult.failure(team_id_validation.exception)
            
            if team_name is not None:
                team_name_validation = NameValidationProcess.execute(team_name)
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
                coord_validation = CoordValidationProcess.execute(coord)
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
