# src/chess/team/team.py
"""
Module: chess.team.team
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0

# SCOPE:
-------
***Limitation 1***: No validation, error checking is performed in `Team` class. Using the class directly instead of
  its CRUD interfaces goes against recommended usage.

***Limitation 2***: There is no guarantee properly created `Team` objects released by the module will satisfy client
    requirements. Clients are responsible for ensuring a `TeamBuilder` product will not fail when used. Products
    from `TeamBuilder` --should-- satisfy `TeamValidator` requirements.

**Related Features**:
    Authenticating existing teams -> See TeamValidator, module[chess.team.validator],
    Handling process and rolling back failures --> See `Transaction`, module[chess.system]

# THEME:
-------
* Data Holding, Coordination, Performance

**Design Concepts**:
    Separating object creation from object usage.
    Keeping constructors lightweight

# PURPOSE:
---------
1. Putting all the steps and logging into one place makes modules using `Team` objects cleaner and easier to follow.

***Satisfies***: Reliability and performance contracts.

# DEPENDENCIES:
---------------
From `chess.system`:
    `BuildResult`, `Builder`, `LoggingLevelRouter`, `ChessException`, `NullException`, `BuildFailedException`
    `IdValidator`, `NameValidator`

From `chess.team`:
    `Team`, `NullTeam`, `TeamBuildFailedException`, `TeamSchema`

From `chess.commander`:
  `Commander`, `CommanderValidator`,

From `chess.piece`:
  `Piece`

# CONTAINS:
----------
 * `Team`
"""


from typing import Optional

from chess.coord import Coord, CoordValidator
from chess.rank import Rank, RankValidator, RankSpec
from chess.team import  RosterNumberOutOfBoundsException, ROSTER_SIZE
from chess.system import (
    IdValidator, NameValidator, Builder, BuildResult,
    MutuallyExclusiveParamsException, AllParamsSetNullException, LoggingLevelRouter
)
from chess.team.search.context.context import BoardSearchContext
from chess.team.search import RansomOutOfBoundsException


class BoardSearchContextBuilder(Builder[BoardSearchContext]):
    """
    # ROLE: Builder implementation

    # RESPONSIBILITIES:
    1. Process and validate parameters for creating `Team` instances.
    2. Create new `Team` objects if parameters meet specifications.
    2. Report errors and return `BuildResult` with error details.

    # PROVIDES:
    `BuildResult`: Return type containing the built `Team` or error information.

    # ATTRIBUTES:
    None
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def build (cls, id: Optional[int], name: Optional[str], coord: Optional[Coord]) -> BuildResult[BoardSearchContext]:
        """
        Action:
        Parameters:
        Returns:
        Raises:
        MethodNameException wraps
        """
        method = "BoardSearchContextBuilder.build"
        try:
            params = [id, name, coord]
            param_count = sum(bool(p) for p in params)

            if param_count == 0:
                return BuildResult(exception=AllParamsSetNullException(
                        f"{method}: {AllParamsSetNullException.DEFAULT_MESSAGE}"
                    )
                )

            if param_count > 1:
                return BuildResult(exception=MutuallyExclusiveParamsException(
                    f"{method}: {MutuallyExclusiveParamsException.DEFAULT_MESSAGE}"
                    )
                )

            if id is not None:
                id_validation = IdValidator.validate(id)
                if not id_validation.is_success():
                    return BuildResult(exception=id_validation.exception)
                return BuildResult(payload=BoardSearchContext(id=id_validation.payload))

            if coord is not None:
                coord_validation =CoordValidator.validate(coord)
                if not coord_validation.is_success():
                    return BuildResult(exception=RosterNumberOutOfBoundsException(
                            f"{method}: {RosterNumberOutOfBoundsException.DEFAULT_MESSAGE}"
                        )
                    )
                return BuildResult(payload=BoardSearchContext(coord=coord))

            if name is not None:
                name_validation = NameValidator.validate(name)
                if not name_validation.is_success():
                    return BuildResult(exception=name_validation.exception)
                return BuildResult(payload=BoardSearchContext(name=name))
        except Exception as e:
            return BuildResult(exception=e)
