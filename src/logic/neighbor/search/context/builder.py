# src/logic/neighbor/searcher/process.py

"""
Module: logic.neighbor.searcher.builder
Author: Banji Lawal
Created: 2025-11-05
version: 1.0.0
"""

from typing import Optional

from logic.coord import Coord, CoordValidationProcess
from logic.rank import Queen, RankSpec
from logic.system import BuildResult, BuildProcess, IdValidationProcess, LoggingLevelRouter, NameValidationProcess
from logic.neighbor import (
    VisitationSearchContext, ArenaVisitationSearchParamsException, ZeroVisitationSearchParamsException, VisitationInvalidRankNameParamException,
)

class VisitationSearchContextBuildProcess(BuildProcess[VisitationSearchContext]):
    """iece
    Role:BuildProcess, Data Integrity And Reliability Guarantor implementation

    Responsibilities:
    1. Process and validate parameters for creating `VisitationSearchContext` instances.
    2. Create new `VisitationSearchContext` objects if parameters meet specifications.
    2. Report errors and return `BuildResult` with error details.

    # PROVIDES:
    `BuildResult`: Return type containing the built `VisitationSearchContext` or error information.

    # ATTRIBUTES:
    None
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def execute (
        cls,
        name: Optional[str] = None,
        ransom: Optional[int] = None,
        piece_id: Optional[int] = None,
        team_id: Optional[id] = None,
        team_name: Optional[str] = None,
        rank_name: Optional[Rank] = None,
        position: Optional[Coord] = None,
    ) -> BuildResult[VisitationSearchContext]:
        """
        ACTION:
        PARAMETERS:
        RETURNS:
        RAISES:
        MethodNameException wraps
        """
        method = "VisitationSearchContextBuildProcess.builder"

        try:
            params = [name, ransom, piece_id, team_id, team_name, rank_name, position]
            param_count = sum(bool(p) for p in params)

            if param_count == 0:
                return BuildResult.failure(
                    ZeroVisitationSearchParamsException(f"{method}: {ZeroVisitationSearchParamsException.MSG}")
                )

            if param_count > 1:
                return BuildResult(
                    ArenaVisitationSearchParamsException(f"{method}: {ArenaVisitationSearchParamsException.MSG}")
                )

            if piece_id is not None:
                id_validation = IdValidationProcess.execute(piece_id)
                if not id_validation.is_failure():
                    return BuildResult(exception=id_validation.exception)

            if name is not None:
                piece_name_validation = NameValidationProcess.execute(name)
                if piece_name_validation.is_failure():
                    return BuildResult(exception=piece_name_validation.exception)

            if team_id is not None:
                team_id_validation = IdValidationProcess.execute(team_id)
                if team_id_validation.is_failure():
                    return BuildResult(exception=team_id_validation.exception)

            if team_name is not None:
                team_name_validation = NameValidationProcess.execute(team_name)
                if team_name_validation.is_failure():
                    return BuildResult.failure(team_name_validation.exception)

            if rank_name is not None and rank_name.upper() not in Persona.__members__:
                return BuildResult.failure(
                    VisitationInvalidRankNameParamException(f"{method}: {VisitationInvalidRankNameParamException.MSG}")
                )

            if ransom not in range[Queen.ransom]:
                return BuildResult.failure(
                    VisitationInvalidRankNameParamException(f"{method}: {VisitationInvalidRankNameParamException.MSG}")
                )

            if position is not None:
                position_validation = CoordValidationProcess.execute(position)
                if position_validation.is_failure():
                    return BuildResult.failure(position_validation.exception)

            return BuildResult.success(
                VisitationSearchContext(
                    name=name,
                    ransom=ransom,
                    piece_id=piece_id,
                    team_id=team_id,
                    team_name=team_name,
                    rank_name=rank_name,
                    position=position
                )
            )
        except Exception as e:
            return BuildResult.failure(e)