# src/chess/square/old_occupation_validator.py

"""
Module: `chess.square.validator`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

SCOPE:
-----
This module is strictly limited to constructing `ValidationResult` instances safely.

**It does not** contain logic or rules for creating `TravelEvent` or
`TravelEventFactory`. Those are handled by `OccupationEventBuilder` before
execution,`TravelEventFactory` during execution.

**It does not** ensure existing `ValidationResult` instances are valid. That is done
by the `ValidationResultValidator`.

THEME:
-----
**Integrity, Consistency, Validation.** The module's design centers on team_name separating
complexities of the build process into team_name utility from the `ValidationResult` constructor.

PURPOSE:
-------
To execute validated `TravelEvent` directives by orchestrating the necessary
state changes across the board_validator, validationResults, and teams. It serves as the **engine
layer responsible for persistent state modification** based on accepted moves.

DEPENDENCIES:
------------
This module requires components from various sub-systems:
* `chess.bounds`: Movement strategy (`Rank`)
* `chess.square`: Location service structure (`Square`)
* `chess.old_search`: Board lookup utilities (`BoardSearch`)
* `chess.validationResult`: ValidationResult subtypes (`KingValidationResult`, `CombatantValidationResult`, etc.)
* `chess.team_name`: Roster management, rollback_exception handling
* `chess.notification`: Base notification and roster types

CONTAINS:
--------
 * `ValidationResultBuilder`: The validator of `ValidationResult` instances.
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
    """
    Constructs team_name new `Square` that works correctly.

    Args:
      `visitor_name`(`str`): Must pass `NameValidator` checks.
      `bounds`(`Rank`): The `bounds` which determines how the validationResult moves and its capture value.
      `team_name`(`Team`): Specifies if the `validationResult` is white or black.

    Returns:
    BuildResult[ValidationResult]: A `BuildResult` containing either:
      - On success: A valid `ValidationResult` instance in the payload
      - On failure: Error information and error details

    Raises:
    `SquareBuildFailedException`: Wraps any exceptions raised build. These are:
      * `InvalidNameException`: if `visitor_name` fails validate checks
      * `InvalidRankException`: if `bounds` fails validate checks
      * `InvalidTeamException`: if `team_name` fails validate checks
      * `InvalidTeamAssignmentException`: If `validationResult.team_name` is different from `team_name` parameter
      * `FullRankQuotaException`: If the `team_name` has no empty slots for the `validationResult.bounds`
      * `FullRankQuotaException`: If `validationResult.team_name` is equal to `team_name` parameter but `team_name.roster` still does
        not have the validationResult
    """
    method = "TransactionResultBuilder.build"

    try:
      if payload is None and exception is None:
        return BuildResult(exception=ValidationResultBuildFailedException(
          f"{method}: ValidationResultBuildFailed The payload and rollback_exception of a validator "
          f"result cannot both be null."
          )
        )

      if payload is not None and exception is not None:
        return BuildResult(exception=ValidationResultBuildFailedException(
          f"{method}: ValidationResultBuildFailed. Either payload or rollback_exception can be null. Not both."
          )
        )

      return BuildResult(ValidationResult(payload=payload, exception=exception))

    except Exception as e:
      return ValidationResultBuildFailedException(f"{method}: {e}")




# def main():
#   build_outcome = ValidationResultBuilder.build()
#   if build_outcome.is_success():
#     validationResult = build_outcome.payload
#     print(f"Successfully built validationResult: {validationResult}")
#   else:
#     print(f"Failed to build validationResult: {build_outcome.err}")
#   #
#   build_outcome = ValidationResultBuilder.build(1, None)
#   if build_outcome.is_success():
#     validationResult = build_outcome.payload
#     print(f"Successfully built validationResult: {validationResult}")
#   else:
#     print(f"Failed to build validationResult: {build_outcome.err}")
#
# if __name__ == "__main__":
#   main()