from enum import Enum

from chess.team import Team, TeamSchema, NullTeamSchemaException, TeamBuilderException
from chess.commander import Commander, CommanderValidator, InvalidCommanderAssignmentException
from chess.system import IdValidator, BuildResult
from chess.exception import RelationshipException
from assurance import ThrowHelper


class TeamBuilder(Enum):
  """
  Builder class responsible for safely constructing `Team` instances.

  `TeamBuilder` ensures that `Team` objects are always created successfully by performing comprehensive validate
   checks during construction. This separates the responsibility of building from validating - `TeamBuilder`
   focuses on creating while `TeamValidator` is used for validating existing `Team` instances that are passed
   around the system.

  The build runs through all validate checks individually to guarantee that any `Team` instance it produces
  meets all required specifications before construction completes

  Usage:
    ```python
    # Safe team creation with validate
    build_result = TeamBuilder.build(team_id=1, commander=black_commander, profile=TeamProfile.BLACK)

    if build_result.is_success():
      team = build_result.payload
    ```

  See Also:
    `Team`: The data structure being constructed
    `TeamValidator`: Used for validating existing `Team` instances
    `BuildResult`: Return type containing the built `Team` or error information
  """


  @staticmethod
  def build(team_id: int, commander: Commander, profile: TeamSchema) -> BuildResult[Team]:
    """
    Constructs a new `Team` instance with comprehensive checks on the parameters and states during the
    build process.

    Performs individual validate checks on each component to ensure the resulting `Team` meets all specifications.
    If all checks are passed, a `Team` instance will be returned. It is not necessary to perform any additional
    validate checks on the returned `Team` instance. This method guarantees if a `BuildResult` with a successful
    status is returned, the contained `Team` is valid and ready for use.

    Args:
      `team_id`(`int`): The unique id for the team. Must pass `IdValidator` checks.
      `commander`(`Commander`): The human or cybernetic moving pieces in `Team.roster`. The commander must pass
        `CommanderValidator` checks.must pass `CommanderValidator` checks.
      `profile`(`TeamProfile`): The profile defining team attributes and behaviors. Must not be None and be
        an instance of `TeamProfile`.

    Returns:
      BuildResult[Team]: A `BuildResult` containing either:
        - On success: A valid `Team` instance in the payload
        - On failure: Error information and error details

    Raises:
      `TeamBuilderException`: Wraps any underlying validate failures that occur during the construction process.
      This includes:
        * `InvalidIdException`: if `id` fails validate checks`
        * `InvalidCommanderException`: if `commander` fails validate checks
        * `NullTeamProfileException`: if `profile` is None
        * `TypeError`: if `profile` is not a `TeamProfile` instance
        * `RelationshipException`: if the bidirectional relationship between `Team` and `Commander` is broken

    Note:
      The build runs through all the checks on parameters and state to guarantee only a valid `Team` is
      created, while `TeamValidator` is used for validating `Team` instances that are passed around after
      creation. This separation of concerns makes the validate and building independent of each other and
      simplifies maintenance.

    Example:
      ```python
      # Valid team creation
      result = TeamBuilder.build(team_id=1, commander=black-commander, profile=black_team_profile)
      if result.is_success():
        team = cast(Team, result.payload) # Guaranteed valid Team

      # Null commander will fail gracefully
      result = TeamBuilder.build(team_id=1, commander=None, profile=black_team_profile)
      if not result.is_success():
        # Handle construction failure
        pass
      ```
    """
    method = "TeamBuilder.build"

    try:
      if profile is None:
        ThrowHelper.propagate_error(
          TeamBuilder, NullTeamSchemaException(NullTeamSchemaException.DEFAULT_MESSAGE)
        )
      if not isinstance(profile, TeamSchema):
        ThrowHelper.propagate_error(
          TeamBuilder, TypeError(f"{method} Expected a TeamProfile, got {type(profile).__name__}")
        )

      id_validation = IdValidator.validate(team_id)
      if not id_validation.is_success():
        ThrowHelper.propagate_error(TeamBuilder, id_validation.exception)


      commander_validation = CommanderValidator.validate(commander)
      if not commander_validation.is_success():
        ThrowHelper.propagate_error(TeamBuilder, commander_validation.exception)

      team = Team(team_id=team_id, commander=commander, schema=profile)

      if team.commander != commander:
        ThrowHelper.propagate_error(
          TeamBuilder,
          InvalidCommanderAssignmentException(InvalidCommanderAssignmentException.DEFAULT_MESSAGE)
        )

      if team not in commander.teams:
        commander.teams.add_team(team)


      if team not in commander.teams:
        ThrowHelper.propagate_error(
          TeamBuilder,
          RelationshipException(RelationshipException.DEFAULT_MESSAGE)
        )


      return BuildResult(payload=team)

    except Exception as e:
      raise TeamBuilderException(f"{method}: {TeamBuilderException.DEFAULT_MESSAGE}") from e

#
# def main():
#   build_result = TeamBuilder.build()
#   if build_result.is_success():
#     team = build_result.payload
#     print(f"Successfully built team: {team}")
#   else:
#     print(f"Failed to build team: {build_result.err}")
#
#   build_result = TeamBuilder.build(-1)
#   if build_result.is_success():
#     team = build_result.payload
#     print(f"Successfully built team: {team}")
#   else:
#     print(f"Failed to build team: {build_result.err}")
#
# if __name__ == "__main__":
#   main()