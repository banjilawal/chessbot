from enum import Enum

from chess.team import Team, TeamProfile, NullTeamProfileException, TeamBuilderException
from chess.commander import Commander, CommanderValidator, InvalidCommanderAssignmentException
from chess.common import IdValidator, BuildResult
from chess.exception import RelationshipException
from assurance import ThrowHelper


class TeamBuilder(Enum):
    """
    Builder class responsible for safely constructing `Team` instances.

    `TeamBuilder` ensures that `Team` objects are always created successfully by
    performing comprehensive validation checks during construction. This separates
    the responsibility of building from validating - `TeamBuilder` focuses on
    creation while `TeamValidator` is used for validating existing `Team` instances
    that are passed around the system.

    The builder runs through all validation checks individually to guarantee that
    any `Team` instance it produces meets all required specifications before
    construction completes.

    Usage:
        ```python
        # Safe team creation with validation
        build_result = TeamBuilder.build(team_id=1, commander=black_commander, profile=TeamProfile.BLACK)

        if build_result.is_success():
            team = build_result.payload
        ```

    See Also:
        `TeamValidator`: Used for validating existing `Team` instances
        `Team`: The data structure being constructed
        `BuildResult`: Return type containing the built `Team` or error information
    """


    @staticmethod
    def build(team_id: int, commander: Commander, profile: TeamProfile) -> BuildResult[Team]:
        """
        Constructs a new `Team` instance with comprehensive validation.

        Performs individual validation checks on each component to ensure the 
        resulting `Team` meets all specifications. The method validates bounds, 
        null checks, and uses `TeamValidator` for final instance validation 
        before returning a successfully constructed `Team`.

        This method guarantees that if a `BuildResult` with a successful status 
        is returned, the contained `Team` is valid and ready for use.

        Args:
           `team_id`(`int`): The unique id for the team. Must pass `IdValidator` checks.
            `commander`(`Commander`): The human or cybernetic moving pieces in `Team.roster`. The commander
                must not be None and must pass `CommanderValidator` checks.must pass `CommanderValidator` checks.
            `profile`(`TeamProfile`): The profile defining team attributes and behaviors. Must not be None and be
                an instance of `TeamProfile`.

        Returns:
            BuildResult[Team]: A `BuildResult` containing either:
                - On success: A valid `Team` instance in the payload
                - On failure: Error information and exception details

        Raises:
            TeamBuilderException: Wraps any underlying validation failures 
                that occur during the construction process. This includes:
                - `IdValidationException`: if `id` fails validation checks`
                - `CommanderValidationException`: if `commander` fails validation checks
                - `NullTeamProfileException`: if `profile` is None
                - `TypeError`: if `profile` is not a `TeamProfile` instance
                - `RelationshipException`: if the bidirectional relationship between
                    `Team` and `Commander` is broken

        Note:
            The builder performs validation at construction time, while 
            `TeamValidator` is used for validating `Team` instances that 
            are passed around after creation. This separation of concerns 
            makes the validation responsibilities clearer.

        Example:
            ```python
            # Valid team creation
            result = TeamBuilder.build(team_id=1, commander=black-commander, profile=black_team_profile)
            if result.is_success():
                team = cast(Team, result.payload)  # Guaranteed valid Team

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
                ThrowHelper.throw_if_invalid(
                    TeamBuilder, NullTeamProfileException(NullTeamProfileException.DEFAULT_MESSAGE)
                )
            if not isinstance(profile, TeamProfile):
                ThrowHelper.throw_if_invalid(
                    TeamBuilder, TypeError(f"{method} Expected a TeamProfile, got {type(profile).__name__}")
                )

            id_validation = IdValidator.validate(team_id)
            if not id_validation.is_success():
                ThrowHelper.throw_if_invalid(TeamBuilder, id_validation.exception)


            commander_validation = CommanderValidator.validate(commander)
            if not commander_validation.is_success():
                ThrowHelper.throw_if_invalid(TeamBuilder, commander_validation.exception)

            team = Team(team_id=team_id, commander=commander, profile=profile)

            if team.commander != commander:
                ThrowHelper.throw_if_invalid(
                    TeamBuilder,
                    InvalidCommanderAssignmentException(InvalidCommanderAssignmentException.DEFAULT_MESSAGE)
                )

            if team not in commander.teams:
                commander.teams.add_team(team)


            if team not in commander.teams:
                ThrowHelper.throw_if_invalid(
                    TeamBuilder,
                    RelationshipException(RelationshipException.DEFAULT_MESSAGE)
                )


            return BuildResult(payload=team)

        except Exception as e:
            raise TeamBuilderException(f"{method}: {TeamBuilderException.DEFAULT_MESSAGE}") from e

#
# def main():
#     build_result = TeamBuilder.build()
#     if build_result.is_success():
#         team = build_result.payload
#         print(f"Successfully built team: {team}")
#     else:
#         print(f"Failed to build team: {build_result.exception}")
#
#     build_result = TeamBuilder.build(-1)
#     if build_result.is_success():
#         team = build_result.payload
#         print(f"Successfully built team: {team}")
#     else:
#         print(f"Failed to build team: {build_result.exception}")
#
# if __name__ == "__main__":
#     main()