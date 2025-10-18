# chess/square/validator.py

"""
Module: `chess.square.validation`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

SCOPE:
-----
This module is strictly limited to constructing `TransactionResult` instances safely.

**It does not** contain logic or rules for creating `TravelEvent` or
`TravelEventFactory`. Those are handled by `OccupationEventBuilder` before
execution,`TravelEventFactory` during execution.

**It does not** ensure existing `TransactionResult` instances are valid. That is done
by the `TransactionResultValidator`.

THEME:
-----
**Integrity, Consistency, Validation.** The module's design centers on team separating
complexities of the build process into team utility from the `TransactionResult` constructor.

PURPOSE:
-------
To execute validated `TravelEvent` directives by orchestrating the necessary
state changes across the board_validator, transactionResults, and teams. It serves as the **engine
layer responsible for persistent state modification** based on accepted moves.

DEPENDENCIES:
------------
This module requires components from various sub-systems:
* `chess.rank`: Movement strategy (`Rank`)
* `chess.square`: Location data structure (`Square`)
* `chess.old_search`: Board lookup utilities (`BoardSearch`)
* `chess.transactionResult`: TransactionResult subtypes (`KingTransactionResult`, `CombatantTransactionResult`, etc.)
* `chess.team`: Roster management, exception handling
* `chess.transaction`: Base transaction and roster types

CONTAINS:
--------
 * `TransactionResultBuilder`: The validation of `TransactionResult` instances.
"""

from typing import TypeVar, Generic

from chess.system import (
  Builder, BuildResult, TransactionResult, LoggingLevelRouter, TransactionResultBuildFailedException, TransactionState
)

T = TypeVar('T')

class TransactionResultBuilder(Builder[TransactionResult[Generic[T]]]):
  """
  Responsible for safely constructing `Square` instances.
  """


  @classmethod
  @LoggingLevelRouter.monitor
  def build(cls, payload: T, exception: Exception, state: TransactionState) -> BuildResult[TransactionResult]:
    """
    Constructs team new `Square` that works correctly.

    Args:
      `name`(`str`): Must pass `NameValidator` checks.
      `rank`(`Rank`): The `rank` which determines how the transactionResult moves and its capture value.
      `team`(`Team`): Specifies if the `transactionResult` is white or black.

    Returns:
    BuildResult[TransactionResult]: A `BuildResult` containing either:
      - On success: A valid `TransactionResult` instance in the payload
      - On failure: Error information and error details

    Raises:
    `SquareBuildFailedException`: Wraps any exceptions raised build. These are:
      * `InvalidNameException`: if `name` fails validate checks
      * `InvalidRankException`: if `rank` fails validate checks
      * `InvalidTeamException`: if `team` fails validate checks
      * `InvalidTeamAssignmentException`: If `transactionResult.team` is different from `team` parameter
      * `FullRankQuotaException`: If the `team` has no empty slots for the `transactionResult.rank`
      * `FullRankQuotaException`: If `transactionResult.team` is equal to `team` parameter but `team.roster` still does
        not have the transactionResult
    """
    method = "TransactionResultBuilder.build"

    try:

      if payload is None:
        return BuildResult(exception=TransactionResultBuildFailedException(
          f"{method}: TransactionResultBuildFailed. event_update cannot be null."
          )
        )

      return BuildResult(TransactionResult(payload=payload, exception=exception, state=state))

    except Exception as e:
      return BuildResult(exception=e)



# def main():
#   build_outcome = TransactionResultBuilder.build()
#   if build_outcome.is_success():
#     transactionResult = build_outcome.payload
#     print(f"Successfully built transactionResult: {transactionResult}")
#   else:
#     print(f"Failed to build transactionResult: {build_outcome.err}")
#   #
#   build_outcome = TransactionResultBuilder.build(1, None)
#   if build_outcome.is_success():
#     transactionResult = build_outcome.payload
#     print(f"Successfully built transactionResult: {transactionResult}")
#   else:
#     print(f"Failed to build transactionResult: {build_outcome.err}")
#
# if __name__ == "__main__":
#   main()