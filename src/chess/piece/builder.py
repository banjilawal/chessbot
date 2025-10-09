# chess/square/builder.py

"""
Module: `chess.square.builder`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

SCOPE:
-----
This module is strictly limited to constructing `Piece` instances safely.

**It does not** contain logic or rules for creating `OccupationEvent` or
`OccupationTransaction`. Those are handled by `OccupationEventBuilder` before
execution,`OccupationTransaction` during execution.

**It does not** ensure existing `Piece` instances are valid. That is done
by the `PieceValidator`.

THEME:
-----
**Integrity, Consistency, Validation.** The module's design centers on team separating
complexities of the build process into team utility from the `Piece` constructor.

PURPOSE:
-------
To execute validated `OccupationEvent` directives by orchestrating the necessary
state changes across the board, pieces, and teams. It serves as the **engine
layer responsible for persistent state modification** based on accepted moves.

DEPENDENCIES:
------------
This module requires components from various sub-systems:
* `chess.rank`: Movement strategy (`Rank`)
* `chess.square`: Location data structure (`Square`)
* `chess.search`: Board lookup utilities (`BoardSearch`)
* `chess.piece`: Piece subtypes (`KingPiece`, `CombatantPiece`, etc.)
* `chess.team`: Roster management, exception handling
* `chess.transaction`: Base transaction and roster types

CONTAINS:
--------
 * `PieceBuilder`: The builder of `Piece` instances.
"""

from chess.system import Builder, BuildResult, NameValidator, LoggingLevelRouter
from chess.piece import Piece, PieceBuildFailedException
from chess.rank import Rank, RankValidator
from chess.team import Team, TeamValidator

class PieceBuilder(Builder[Piece]):
  """
  Responsible for safely constructing `Square` instances.
  """

  @classmethod
  def build(cls, name: str, rank: Rank, team: Team) -> BuildResult[Piece]:
    """
    Constructs team new `Square` that works correctly.

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
      #   LoggingLevelRouter.throw_if_invalid(PieceBuilder, id_validation)

      name_validation = NameValidator.validate(name)
      if not name_validation.is_success():
        LoggingLevelRouter.log_and_raise_error(PieceBuilder, name_validation.exception)

      rank_validation = RankValidator.validate(rank)
      if not rank_validation.is_success():
        LoggingLevelRouter.log_and_raise_error(PieceBuilder, rank_validation.exception)

      team_validation = TeamValidator.validate(team)
      if not team_validation.is_success():
        LoggingLevelRouter.log_and_raise_error(PieceBuilder, team_validation.exception)

      if len(TeamSearch.by_rank(rank, team).payload) >= rank.quota:
        LoggingLevelRouter.log_and_raise_error(
          PieceBuilder,
          FullRankQuotaException(FullRankQuotaException.DEFAULT_MESSAGE)
        )

      piece = None
      if isinstance(rank, King):
        piece = KingPiece(name=name, rank=rank, team=team)
      else:
        piece = CombatantPiece(name=name, rank=rank, team=team)

      if not piece.team == team:
        LoggingLevelRouter.log_and_raise_error(
          PieceBuilder,
          ConflictingTeamAssignmentException(ConflictingTeamAssignmentException.DEFAULT_MESSAGE)
        )

      if not piece.team == team:
        team.add_to_roster(piece)

      if piece not in team.roster:
        LoggingLevelRouter.log_and_raise_error(
          PieceBuilder,
          UnregisteredTeamMemberException(UnregisteredTeamMemberException.DEFAULT_MESSAGE)
        )

      return BuildResult(payload=piece)
    except Exception as e:
      raise PieceBuilderException(f"{method}: {e}") for e



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