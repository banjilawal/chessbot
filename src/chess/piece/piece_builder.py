from enum import Enum
from typing import cast

from chess.rank import Rank
from assurance import ThrowHelper

from chess.exception import RelationshipException
from chess.common import IdValidator, NameValidator, BuildResult
from chess.piece import Piece, PieceValidator, PieceBuilderException
from chess.team import Team, TeamValidator, InvalidTeamAssignmentException


class PieceBuilder(Enum):

    @staticmethod
    def build(piece_id: int, name: str, rank: Rank, team: Team) -> BuildResult[Piece]:

        method = "PieceBuilder.build"

        try:
            id_validation = IdValidator.validate(piece_id)
            if not id_validation.is_success():
                ThrowHelper.throw_if_invalid(PieceBuilder, id_validation)
            piece_id = cast(int, id_validation.payload)

            name_validation = NameValidator.validate(name)
            if not name_validation.is_success():
                ThrowHelper.throw_if_invalid(PieceBuilder, name_validation)
            name = cast(str, name_validation.payload)

            team_validation = TeamValidator.validate(team)
            if not team_validation.is_success():
                ThrowHelper.throw_if_invalid(PieceBuilder, team_validation)
            team = cast(Team, team_validation.payload)

            piece_validation = PieceValidator.validate(Piece(piece_id=piece_id, name=name, rank=rank, team=team))
            if not piece_validation.is_success():
                ThrowHelper.throw_if_invalid(PieceBuilder, piece_validation)
            piece = cast(Piece, piece_validation.payload)

            if not piece.team == team:
                ThrowHelper.throw_if_invalid(
                    PieceBuilder,
                    InvalidTeamAssignmentException(InvalidTeamAssignmentException.DEFAULT_MESSAGE)
                )

            if piece not in team.roster:
                team.add_to_roster(piece)

            if piece not in team.roster:
                ThrowHelper.throw_if_invalid(
                    PieceBuilder,
                    RelationshipException(RelationshipException.DEFAULT_MESSAGE)
                )

            return BuildResult(payload=piece)
        except Exception as e:
            raise PieceBuilderException(f"{method}: {PieceBuilderException}")


# def main():
#     build_result = PieceBuilder.build()
#     if build_result.is_success():
#         piece = build_result.payload
#         print(f"Successfully built piece: {piece}")
#     else:
#         print(f"Failed to build piece: {build_result.exception}")
#     #
#     build_result = PieceBuilder.build(1, None)
#     if build_result.is_success():
#         piece = build_result.payload
#         print(f"Successfully built piece: {piece}")
#     else:
#         print(f"Failed to build piece: {build_result.exception}")
#
# if __name__ == "__main__":
#     main()