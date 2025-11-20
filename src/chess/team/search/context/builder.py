
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


    @classmethod
    def build (
        cls,
        name: Optional[str],
        rank: Optional[Rank],
        ransom: Optional[int],
        piece_id: Optional[int],
        roster_number: Optional[int],
    ) -> BuildResult[TeamSearchContext]:

        method = "PieceSearchContextBuilder.builder"

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