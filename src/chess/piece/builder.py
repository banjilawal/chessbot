from enum import Enum

from chess.system import BuildResult, NameValidator, ThrowHelper

from chess.rank import Rank, King, RankValidator
from chess.piece import Piece, KingPiece, CombatantPiece, UnregisteredTeamMemberException
from chess.team import Team, TeamValidator, TeamSearch, FullRankQuotaException, ConflictingTeamAssignmentException


class PieceBuilder(Enum):
    """
    Builder class responsible for safely constructing `Piece` instances.
    """

    @staticmethod
    def build(piece_id: int, name: str, rank: Rank, team: Team) -> BuildResult[Piece]:
        """
        Constructs a new `Piece` instance with comprehensive checks on the parameters and states during the
        build process.

        Args:
            `name`(`str`): Must pass `NameValidator` checks.
            `rank`(`Rank`): The `rank` which determines how the piece moves and its capture value.
            `team`(`Team`): Specifies if the `piece` is white or black.

        Returns:
            BuildResult[Piece]: A `BuildResult` containing either:
                - On success: A valid `Piece` instance in the payload
                - On failure: Error information and exception details

        Raises:
           PieceBuilderException: Wraps any underlying validation failures that occur during the construction process.
           This includes:
                * `InvalidNameException`: if `name` fails validation checks
                * `InvalidRankException`: if `rank` fails validation checks
                * `InvalidTeamException`: if `team` fails validation checks
                * `InvalidTeamAssignmentException`: If `piece.team` is different from `team` parameter
                * `FullRankQuotaException`: If the `team` has no empty slots for the `piece.rank`
                * `FullRankQuotaException`: If `piece.team` is equal to `team` parameter but `team.roster` still does
                    not have the piece
        """
        method = "PieceBuilder.build"

        try:
            # id_validation = IdValidator.validate(piece_id)
            # if not id_validation.is_success():
            #     ThrowHelper.throw_if_invalid(PieceBuilder, id_validation)

            name_validation = NameValidator.validate(name)
            if not name_validation.is_success():
                ThrowHelper.throw_if_invalid(PieceBuilder, name_validation)

            rank_validation = RankValidator.validate(rank)
            if not rank_validation.is_success():
                ThrowHelper.throw_if_invalid(PieceBuilder, rank_validation)

            team_validation = TeamValidator.validate(team)
            if not team_validation.is_success():
                ThrowHelper.throw_if_invalid(PieceBuilder, team_validation)

            if len(TeamSearch.by_rank(rank, team).payload) >= rank.quota:
                ThrowHelper.throw_if_invalid(
                    PieceBuilder,
                    FullRankQuotaException(FullRankQuotaException.DEFAULT_MESSAGE)
                )

            piece = None
            if isinstance(rank, King):
                piece = KingPiece(piece_id=piece_id, name=name, rank=rank, team=team)
            piece = CombatantPiece(piece_id=piece_id, name=name, rank=rank, team=team)

            if not piece.team == team:
                ThrowHelper.throw_if_invalid(
                    PieceBuilder,
                    ConflictingTeamAssignmentException(ConflictingTeamAssignmentException.DEFAULT_MESSAGE)
                )

            if not piece.team == team:
                team.add_to_roster(piece)

            if piece not in team.roster:
                ThrowHelper.throw_if_invalid(
                    PieceBuilder,
                    UnregisteredTeamMemberException(UnregisteredTeamMemberException.DEFAULT_MESSAGE)
                )

            return BuildResult(payload=piece)
        except Exception as e:
            raise PieceBuilderException(f"{method}: {PieceBuilderException.DEFAULT_MESSAGE}")



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