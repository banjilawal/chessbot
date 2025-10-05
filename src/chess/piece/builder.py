# chess/square/builder.py

"""
Module: `chess.square.builder`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

Contains: SquareBuilder
 Provides: Create `Square` instances 
"""
from chess.system import Builder, BuildResult, NameValidator, RaiserLogger

from chess.rank import Rank, King, RankValidator
from chess.piece import Piece, KingPiece, CombatantPiece, UnregisteredTeamMemberException
from chess.team import(
  Team, TeamValidator, TeamSearch, FullRankQuotaException, ConflictingTeamAssignmentException
)


class PieceBuilder(Builder[Piece]):
  """
  Responsible for safely constructing `Square` instances.
  """

  @classmethod
  def build(cls, name: str, rank: Rank, team: Team) -> BuildResult[Piece]:
    """
    Constructs a new `Square` that works correctly.

    Args:
      `name`(`str`): Must pass `NameValidator` checks.
      `rank`(`Rank`): The `rank` which determines how the piece moves and its capture value.
      `team`(`Team`): Specifies if the `piece` is white or black.

    Returns:
    BuildResult[Piece]: A `BuildResult` containing either:
      - On success: A valid `Piece` instance in the payload
      - On failure: Error information and error details

    Raises:
    `SquareBuildFailedException`: Wraps any exceptions raised build. These are:
      * `InvalidNameException`: if `name` fails validate checks
      * `InvalidRankException`: if `rank` fails validate checks
      * `InvalidTeamException`: if `team` fails validate checks
      * `InvalidTeamAssignmentException`: If `piece.team` is different from `team` parameter
      * `FullRankQuotaException`: If the `team` has no empty slots for the `piece.rank`
      * `FullRankQuotaException`: If `piece.team` is equal to `team` parameter but `team.roster` still does
        not have the piece
    """
    method = "PieceBuilder.build"

    try:
      # id_validation = IdValidator.validate(piece_id)
      # if not id_validation.is_success():
      #   RaiserLogger.throw_if_invalid(PieceBuilder, id_validation)

      name_validation = NameValidator.validate(name)
      if not name_validation.is_success():
        RaiserLogger.propagate_error(PieceBuilder, name_validation)

      rank_validation = RankValidator.validate(rank)
      if not rank_validation.is_success():
        RaiserLogger.propagate_error(PieceBuilder, rank_validation)

      team_validation = TeamValidator.validate(team)
      if not team_validation.is_success():
        RaiserLogger.propagate_error(PieceBuilder, team_validation)

      if len(TeamSearch.by_rank(rank, team).payload) >= rank.quota:
        RaiserLogger.propagate_error(
          PieceBuilder,
          FullRankQuotaException(FullRankQuotaException.DEFAULT_MESSAGE)
        )

      piece = None
      if isinstance(rank, King):
        piece = KingPiece(piece_id=piece_id, name=name, rank=rank, team=team)
      piece = CombatantPiece(piece_id=piece_id, name=name, rank=rank, team=team)

      if not piece.team == team:
        RaiserLogger.propagate_error(
          PieceBuilder,
          ConflictingTeamAssignmentException(ConflictingTeamAssignmentException.DEFAULT_MESSAGE)
        )

      if not piece.team == team:
        team.add_to_roster(piece)

      if piece not in team.roster:
        RaiserLogger.propagate_error(
          PieceBuilder,
          UnregisteredTeamMemberException(UnregisteredTeamMemberException.DEFAULT_MESSAGE)
        )

      return BuildResult(payload=piece)
    except Exception as e:
      raise PieceBuilderException(f"{method}: {e}") for



# def main():
#   build_outcome = PieceBuilder.build()
#   if build_outcome.is_success():
#     piece = build_outcome.payload
#     print(f"Successfully built piece: {piece}")
#   else:
#     print(f"Failed to build piece: {build_outcome.err}")
#   #
#   build_outcome = PieceBuilder.build(1, None)
#   if build_outcome.is_success():
#     piece = build_outcome.payload
#     print(f"Successfully built piece: {piece}")
#   else:
#     print(f"Failed to build piece: {build_outcome.err}")
#
# if __name__ == "__main__":
#   main()