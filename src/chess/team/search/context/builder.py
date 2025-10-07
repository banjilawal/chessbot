# src/chess/piece/event/transaction
"""
Module: chess.piece.event.transaction
Author: Banji Lawal
Created: 2025-09-28

# SCOPE:
* The limits of the module, defined by what it does not do.
* Where to look for related features this models does not provide because of its limitations.

# THEME:
* Highlight the core feature (thread-safety)
* Explain the how-and-why of implementation choices.

# PURPOSE:
* Function and role in the system.
* Why the module exists in the application architecture
* What problem it fundamentally solves

# DEPENDENCIES:

# CONTAINS:
 * ``
"""


from typing import Optional

from chess.rank import Rank, RankValidator, RankSpec
from chess.team import  RosterNumberOutOfBoundsException, ROSTER_SIZE
from chess.system import (
    IdValidator, NameValidator, Builder, BuildResult,
    MutuallyExclusiveParamsException, AllParamsSetNullException, RaiserLogger
)
from chess.team.search.context.context import PieceSearchContext
from chess.team.search import RansomOutOfBoundsException


class PieceSearchContextBuilder(Builder[PieceSearchContext]):
    """
    ROLE:
    ----
    RESPONSIBILITIES:
    ----------------
    PROVIDES:
    --------
    ATTRIBUTES:
    ----------
    """

    @classmethod
    def build (
        cls,
        name: Optional[str],
        rank: Optional[Rank],
        ransom: Optional[int],
        piece_id: Optional[int],
        roster_number: Optional[int],
    ) -> BuildResult[PieceSearchContext]:
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
                RaiserLogger(PieceSearchContextBuilder, id_validation.exception)
                return BuildResult(exception=id_validation.exception)
            return BuildResult(payload=PieceSearchContext(piece_id=id_validation.payload))

        if roster_number is not None:
            if roster_number < 1 or roster_number > ROSTER_SIZE:
                err = RosterNumberOutOfBoundsException(
                    f"{method}: {RosterNumberOutOfBoundsException.DEFAULT_MESSAGE}"
                )
                RaiserLogger(PieceSearchContextBuilder, err)
                return BuildResult(exception=err)
            return BuildResult(payload=PieceSearchContext(roster_number=roster_number))

        if name is not None:
            name_validation = NameValidator.validate(name)
            if not name_validation.is_success():
                RaiserLogger(PieceSearchContextBuilder, name_validation.exception)
                return BuildResult(exception=name_validation.exception)
            return BuildResult(payload=PieceSearchContext(name=name))

        if ransom is not None:
            if ransom < RankSpec.KING.ransom or ransom > RankSpec.QUEEN.ransom:
                err = RansomOutOfBoundsException(
                    f"{method}: {RansomOutOfBoundsException.DEFAULT_MESSAGE}"
                )
                RaiserLogger(PieceSearchContextBuilder, err)
                return BuildResult(exception=err)
            return BuildResult(payload=PieceSearchContext(ransom=ransom))

        if rank is not None:
            rank_validation = RankValidator.validate(rank)
            if not rank_validation.is_success():
                RaiserLogger(PieceSearchContextBuilder, rank_validation.exception)
                return BuildResult(exception=rank_validation.exception)
            return BuildResult(payload=PieceSearchContext(rank=rank))