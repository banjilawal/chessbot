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

from chess.rank import Rank, RankValidator, RankSpec
from chess.team import  RosterNumberOutOfBoundsException, ROSTER_SIZE
from chess.system import (
    IdValidator, NameValidator, Builder, BuildResult,
    MutuallyExclusiveParamsException, AllParamsSetNullException, LoggingLevelRouter
)
from chess.team.search.context.context import TeamSearchContext
from chess.team.search import RansomOutOfBoundsException


class PieceSearchContextBuilder(Builder[TeamSearchContext]):
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
    def build (
        cls,
        name: Optional[str],
        rank: Optional[Rank],
        ransom: Optional[int],
        piece_id: Optional[int],
        roster_number: Optional[int],
    ) -> BuildResult[TeamSearchContext]:
        """
        Action:
        Parameters:
        Returns:
        Raises:
        MethodNameException wraps
        """
        method = "PieceSearchContextBuilder.build"

        params = [name, rank, ransom, piece_id, roster_number]
        param_count = sum(bool(p) for p in params)

        if param_count == 0:
            raise AllParamsSetNullException(
                f"{method}: {AllParamsSetNullException.DEFAULT_MESSAGE}"
            )

        if param_count > 1:
            raise MutuallyExclusiveParamsException(
                f"{method}: {MutuallyExclusiveParamsException.DEFAULT_MESSAGE}"
            )

        if piece_id is not None:
            id_validation = IdValidator.validate(piece_id)
            if not id_validation.is_success():
                LoggingLevelRouter(PieceSearchContextBuilder, id_validation.exception)
                return BuildResult(exception=id_validation.exception)
            return BuildResult(payload=TeamSearchContext(piece_id=id_validation.payload))

        if roster_number is not None:
            if roster_number < 1 or roster_number > ROSTER_SIZE:
                err = RosterNumberOutOfBoundsException(
                    f"{method}: {RosterNumberOutOfBoundsException.DEFAULT_MESSAGE}"
                )
                LoggingLevelRouter(PieceSearchContextBuilder, err)
                return BuildResult(exception=err)
            return BuildResult(payload=TeamSearchContext(roster_number=roster_number))

        if name is not None:
            name_validation = NameValidator.validate(name)
            if not name_validation.is_success():
                LoggingLevelRouter(PieceSearchContextBuilder, name_validation.exception)
                return BuildResult(exception=name_validation.exception)
            return BuildResult(payload=TeamSearchContext(name=name))

        if ransom is not None:
            if ransom < RankSpec.KING.ransom or ransom > RankSpec.QUEEN.ransom:
                err = RansomOutOfBoundsException(
                    f"{method}: {RansomOutOfBoundsException.DEFAULT_MESSAGE}"
                )
                LoggingLevelRouter(PieceSearchContextBuilder, err)
                return BuildResult(exception=err)
            return BuildResult(payload=TeamSearchContext(ransom=ransom))

        if rank is not None:
            rank_validation = RankValidator.validate(rank)
            if not rank_validation.is_success():
                LoggingLevelRouter(PieceSearchContextBuilder, rank_validation.exception)
                return BuildResult(exception=rank_validation.exception)
            return BuildResult(payload=TeamSearchContext(rank=rank))