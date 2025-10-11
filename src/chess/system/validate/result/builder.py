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

from typing import TypeVar, Generic

from chess.system import Builder, BuildResult, ValidationResult, LoggingLevelRouter, ValidationResultBuildFailedException

T = TypeVar('T')

class ValidationResultBuilder(Builder[ValidationResult[Generic[T]]]):
  """
  Responsible for safely constructing `Square` instances.
  """


  @classmethod
  @LoggingLevelRouter.monitor
  def build(cls, payload: T, exception: Exception) -> BuildResult[ValidationResult]:

    method = "TransactionResultBuilder.build"

    try:
      if payload is None and exception is None:
        return BuildResult(exception=ValidationResultBuildFailedException(
          f"{method}: ValidationResultBuildFailed The payload and exception of a validation "
          f"result cannot both be null."
          )
        )

      if payload is not None and exception is not None:
        return BuildResult(exception=ValidationResultBuildFailedException(
          f"{method}: ValidationResultBuildFailed. Either payload or exception can be null. Not both."
          )
        )

      return BuildResult(ValidationResult(payload=payload, exception=exception))

    except Exception as e:
      return ValidationResultBuildFailedException(f"{method}: {e}")

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