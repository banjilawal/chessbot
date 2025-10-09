# src/chess/team/builder.py

"""
Module: chess.team.builder
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0

# SCOPE:
-------
***Limitation***: There is no guarantee properly created `Team` objects released by the module will satisfy
    client requirements. Clients are responsible for ensuring a `TeamBuilder` product will not fail when used. 

**Related Features**:
    Authenticating existing teams -> See TeamValidator, module[chess.team.validator],
    Handling process and rolling back failures --> See `Transaction`, module[chess.system]

# THEME:
-------
* Data assurance, error prevention

**Design Concepts**:
    Separating object creation from object usage. 
    Keeping constructors lightweight

# PURPOSE:
---------
1. Central, single producer of authenticated `Team` objects.
2. Putting all the steps and logging into one place makes modules using `Team` objects cleaner and easier to follow.

**Satisfies**: Reliability and performance contracts.

# DEPENDENCIES:
---------------
From `chess.system`:
    `BuildResult`, `Builder`, `LoggingLevelRouter`, `ChessException`, `NullException`, `BuildFailedException`
    `IdValidator`, `NameValidator`

From `chess.team`:
    `Team`, `NullTeam`, `TeamBuildFailedException`, `TeamSchema`

From `chess.commander`:
  `Commander`, `CommanderValidator`,

# CONTAINS:
----------
 * `TeamBuilder`
"""


from chess.team import Team, TeamSchema, NullTeamSchemaException, TeamBuildFailedException
from chess.commander import Commander, CommanderValidator, InvalidCommanderAssignmentException
from chess.system import IdValidator, BuildResult, Builder, LoggingLevelRouter
from chess.exception import RelationshipException


class TeamBuilder(Builder[Team]):
  """
  # ROLE: Builder

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
  def build(cls, commander: Commander, schema: TeamSchema) -> BuildResult[Team]:
    """
    ACTION:
    Create a `Team` object if the parameters have correctness.

    PARAMETERS:
        * `commander` (`Commander`): owner of `Team` object.
        * `schema` (`iTeamSchema`): Spec about the team's color, starting squares etc.

    RETURNS:
    `BuildResult[Team]`: A `BuildResult` containing either:
        `'payload'` - A valid `Team` instance in the payload
        `exception` - Error information and error details

    RAISES:
    `TeamBuildFailedException`: Wraps any specification violations including:
        * `NullXComponentException`: if `x` is None
        * `NullYComponentException`: if `y` is None
        * `TeamBelowBoundsException`: if `x` or `y` < -KNIGHT_STEP_SIZE
        * `TeamAboveBoundsException`: if `x` or `y` > KNIGHT_STEP_SIZE
    """
    method = "TeamBuilder.build"

    try:
      if schema is None:
        return BuildResult(exception=NullTeamSchemaException(NullTeamSchemaException.DEFAULT_MESSAGE)
                            )
      if not isinstance(schema, TeamSchema):
        return BuildResult(exception=TypeError(
          f"{method} Expected team TeamProfile, got {type(schema).__name__}"
        ))

      id_validation = IdValidator.validate(team_id)
      if not id_validation.is_success():
        ThrowHelper.log_and_raise_error(TeamBuilder, id_validation.exception)


      commander_validation = CommanderValidator.validate(commander)
      if not commander_validation.is_success():
        return BuildResult(exception=commander_validation.exception)

      team = Team(commander=commander, schema=schema)

      if team.commander != commander:
        return BuildResult(exception=InvalidCommanderAssignmentException(
          InvalidCommanderAssignmentException.DEFAULT_MESSAGE
        ))

      if team not in commander.teams:
        commander.teams.add_team(team)

      if team not in commander.teams:
        return BuildResult(exception=RelationshipException(RelationshipException.DEFAULT_MESSAGE))

      return BuildResult(payload=team)

    except Exception as e:
      return BuildResult(exception=TeamBuildFailedException(f"{method}: {e}"))