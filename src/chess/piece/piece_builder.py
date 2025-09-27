from enum import Enum

from chess.rank import Rank, King, RankValidator
from assurance import ThrowHelper

from chess.exception import RelationshipException
from chess.common import IdValidator, NameValidator, BuildResult
from chess.piece import Piece, KingPiece, CombatantPiece, PieceBuilderException
from chess.team import Team, TeamValidator, InvalidTeamAssignmentException


class PieceBuilder(Enum):
    """
    Builder class responsible for safely constructing `Piece` instances.
    
    `PieceBuilder` ensures that `Piece` objects are always created successfully by
    performing comprehensive validation checks during construction. This separates
    the responsibility of building from validating - `PieceBuilder` focuses on
    creation while `PieceValidator` is used for validating existing `Piece` instances
    that are passed around the system.
    
    The builder runs through all validation checks individually to guarantee that
    any `Piece` instance it produces meets all required specifications before
    construction completes.
    
    Usage:
        ```python
        # Safe piece creation with validation
        build_outcome = PieceBuilder.build(piece_id=id_emitter.piece_id, name="WN2", rank=Knight(), team=white_team)
        if not build_outcome.is_success():
            raise build_outcome.exception
        piece = build_outcome.payload
        ```
    
    See Also:
        `PieceValidator`: Used for validating existing `Piece` instances
        `Piece`: The data structure being constructed
        `BuildResult`: Return type containing the built `Piece` or error information
    """

    @staticmethod
    def build(piece_id: int, name: str, rank: Rank, team: Team) -> BuildResult[Piece]:

        method = "PieceBuilder.build"

        try:
            id_validation = IdValidator.validate(piece_id)
            if not id_validation.is_success():
                ThrowHelper.throw_if_invalid(PieceBuilder, id_validation)

            name_validation = NameValidator.validate(name)
            if not name_validation.is_success():
                ThrowHelper.throw_if_invalid(PieceBuilder, name_validation)

            rank_validation = RankValidator.validate(rank)
            if not rank_validation.is_success():
                ThrowHelper.throw_if_invalid(PieceBuilder, rank_validation)

            team_validation = TeamValidator.validate(team)
            if not team_validation.is_success():
                ThrowHelper.throw_if_invalid(PieceBuilder, team_validation)


            piece = None
            if isinstance(rank, King):
                piece = KingPiece(piece_id=piece_id, name=name, rank=rank, team=team)
            piece = CombatantPiece(piece_id=piece_id, name=name, rank=rank, team=team)

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
#     build_outcome = PieceBuilder.build()
#     if build_outcome.is_success():
#         piece = build_outcome.payload
#         print(f"Successfully built piece: {piece}")
#     else:
#         print(f"Failed to build piece: {build_outcome.exception}")
#     #
#     build_outcome = PieceBuilder.build(1, None)
#     if build_outcome.is_success():
#         piece = build_outcome.payload
#         print(f"Successfully built piece: {piece}")
#     else:
#         print(f"Failed to build piece: {build_outcome.exception}")
#
# if __name__ == "__main__":
#     main()