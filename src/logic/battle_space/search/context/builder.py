# src/logic/battle_space/searcher/compute.py

"""
Module: logic.battle_space.searcher.builder
Author: Banji Lawal
Created: 2025-10-27
version: 1.0.0
"""


from typing import Optional

from logic.coord import Coord, CoordValidator
from logic.rank import Rank, RankValidator, RankSpec
from logic.team import  RosterNumberOutOfBoundsException, ROSTER_SIZE
from logic.system import (
    IdValidator, NameValidator, Builder, BuildResult,
    MutuallyExclusiveParamsException, AllParamsSetNullException, LoggingLevelRouter
)
from logic.team.search.context.context import ProjectionSearchContext
from logic.team.search import RansomOutOfBoundsException


class ProjectionSearchContextBuilder(Builder[ProjectionSearchContext]):
    """"""

    @classmethod
    @LoggingLevelRouter.monitor
    def build (cls, id: Optional[int], name: Optional[str], coord: Optional[Coord]) -> BuildResult[ProjectionSearchContext]:
        """"""
        method = "ProjectionSearchContextBuilder.builder"
        try:
            params = [id, name, coord]
            param_count = sum(bool(p) for p in params)

            if param_count == 0:
                return BuildResult(exception=AllParamsSetNullException(
                        f"{method}: {AllParamsSetNullException.MSG}"
                    )
                )

            if param_count > 1:
                return BuildResult(exception=MutuallyExclusiveParamsException(
                    f"{method}: {MutuallyExclusiveParamsException.MSG}"
                    )
                )

            if id is not None:
                id_validation = IdValidator.validate(id)
                if not id_validation.is_success():
                    return BuildResult(exception=id_validation.exception)
                return BuildResult(payload=ProjectionSearchContext(id=id_validation.payload))

            if coord is not None:
                coord_validation =CoordValidator.validate(coord)
                if not coord_validation.is_success():
                    return BuildResult(exception=RosterNumberOutOfBoundsException(
                            f"{method}: {RosterNumberOutOfBoundsException.MSG}"
                        )
                    )
                return BuildResult(payload=ProjectionSearchContext(coord=coord))

            if name is not None:
                name_validation = NameValidator.validate(name)
                if not name_validation.is_success():
                    return BuildResult(exception=name_validation.exception)
                return BuildResult(payload=ProjectionSearchContext(name=name))
        except Exception as e:
            return BuildResult(exception=e)
