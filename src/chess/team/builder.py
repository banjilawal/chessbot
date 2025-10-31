# src/chess/team/builder.py

"""
Module: chess.team.builder
Author: Banji Lawal
Created: 2025-09-04
Updated: 2025-10-08
version: 1.0.0
"""

from chess.team import Team, TeamSchema, TeamSchemaValidator, TeamBuildFailedException
from chess.commander import Commander, CommanderValidator, InvalidCommanderAssignmentException
from chess.system import BuildResult, Builder, LoggingLevelRouter, InconsistentCollectionException


class TeamBuilder(Builder[Team]):
  """
  # ROLE: Builder implementation

  # RESPONSIBILITIES:
  1. Process and validate parameters for creating `Team` instances.
  2. Create new `Team` objects if parameters meet specifications.
  2. Report errors and return `BuildResult` with error details.

  # PROVIDES:
  `BuildResult`: Return type containing the built `Team` or error information.

  # ATTRIBUTES:
  None
  """

  @classmethod
  @LoggingLevelRouter.monitor()
  def build(cls, id: int, commander: Commander, schema: TeamSchema) -> BuildResult[Team]:
    """
    ACTION:
    Create a `Team` object if the parameters have correctness.

    PARAMETERS:
        * `commander` (`Commander`): owner of `Team` object.
        * `schema` (`iTeamSchema`): Spec about the team's color, starting squares etc.

    RETURNS:
    `BuildResult[Team]`: A `BuildResult` containing either:
        `'payload'` - A valid `Team` instance in the payload
        `rollback_exception` - Error information and error details

    RAISES:
    `TeamBuildFailedException`: Wraps any specification violations including:
        * `NullXComponentException`: if `x` is None
        * `NullYComponentException`: if `y` is None
        * `TeamBelowBoundsException`: if `x` or `y` < -KNIGHT_STEP_SIZE
        * `TeamAboveBoundsException`: if `x` or `y` > KNIGHT_STEP_SIZE
    """
    method = "TeamBuilder.build"

    try:
      schema_validation = TeamSchemaValidator.validate(schema)
      if not schema_validation.is_success():
        return BuildResult(exception=schema_validation.exception)

      commander_validation = CommanderValidator.validate(commander)
      if not commander_validation.is_success():
        return BuildResult(exception=commander_validation.exception)

      team = Team(commander=commander, schema=schema)

      if team.commander != commander:
        return BuildResult(exception=InvalidCommanderAssignmentException(
          f"{method}: {InvalidCommanderAssignmentException.DEFAULT_MESSAGE}"
          )
        )

      if team not in commander.teams:
        commander.teams.add_team(team)

      if team not in commander.teams:
        return BuildResult(exception=InconsistentCollectionException(
          f"{method}: [Team-Not-In-Commander-History] {InconsistentCollectionException.DEFAULT_MESSAGE}"
          )
        )

      return BuildResult(payload=team)

    except Exception as e:
      return BuildResult(exception=TeamBuildFailedException(f"{method}: {e}"))