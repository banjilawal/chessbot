from crypt import methods
from typing import cast, Generic, TYPE_CHECKING, TypeVar

from chess.common import Result, Validator, IdValidator, IdValidationException
from chess.exception import RelationshipException
from chess.team import Team, NullTeamException, NullTeamProfileException, TeamValidationException
from chess.commander import Commander, CommanderValidator, CommanderValidationException, \
    InvalidCommanderAssignmentException

T = TypeVar('T')

class TeamValidator(Validator):
    """
    Validates existing `Team` instances that are passed around the system.

    While `TeamBuilder` ensures valid Teams are created, `TeamValidator`
    checks `Team` instances that already exist - whether they came from
    deserialization, external sources, or need re-validation after modifications.
    
    Usage:
        ```python
        # Validate an existing team
        team_validation = TeamValidator.validate(candidate)    
        if not team_validation.is_success():
            raise team_validation.exception
        team = cast(Team, team_validation.payload)
        ```

    Use `TeamBuilder` for construction, `TeamValidator` for verification.
    """

    @staticmethod
    def validate(t: Generic[T]) -> Result['Team']:
        """
        Validates that an existing `Team` instance meets all specifications.

        Performs comprehensive validation on a `Team` instance that already exists,
        checking type safety, null values, and component bounds. Unlike `TeamBuilder`
        which creates new valid Teams, this validator verifies existing `Team`
        instances from external sources, deserialization, or after modifications.

        Args
            `t` (`Team`): `Team` instance to validate

         Returns:
            `Result`[`Team`]: A `Resul`t object containing the validated payload if the specification is satisfied,
            `TeamValidationException` otherwise.

        Raises:
            `TypeError`: if `t` is not a Team` object
            `NullTeamException`: if `t` is null
            `IdValidationException`: if `id` fails validation checks
            `CommanderValidationException`: if `commander` fails validation checks
            `NullTeamProfileException`: if `profile` is null
            `InvalidCommanderAssignmentException`: if the assigned commander does not match the validated commander
            `RelationshipException`: if the bidirectional relationship between Team and Commander is broken
            `TeamValidationException`: Wraps any preceding exceptions
        """
        method = "TeamValidator.validate"

        try:
            if t is None:
                raise NullTeamException(f"{method} {NullTeamException.DEFAULT_MESSAGE}")

            from chess.team import Team
            if not isinstance(t, Team):
                raise TypeError(f"{method} Expected a Team, got {type(t).__name__}")

            team = cast(Team, t)

            if team.profile is None:
                raise NullTeamProfileException(f"{method}: {NullTeamProfileException.DEFAULT_MESSAGE}")

            id_validation = IdValidator.validate(team.id)
            if not id_validation.is_success():
                raise IdValidationException(f"{method}: {IdValidationException.DEFAULT_MESSAGE}")

            commander_validation = CommanderValidator.validate(team.commander)
            if not commander_validation.is_success():
                raise CommanderValidationException(f"{method}: {CommanderValidationException.DEFAULT_MESSAGE}")

            commander = cast(Commander, commander_validation.payload)
            if team.commander != commander:
                raise InvalidCommanderAssignmentException(
                    f"{method}: {InvalidCommanderAssignmentException.DEFAULT_MESSAGE}"
                )

            if team not in commander.teams.items:
                raise RelationshipException(f"{method}: {RelationshipException.DEFAULT_MESSAGE}")

            return Result(payload=team)

        except (
            TypeError,
            NullTeamException,
            IdValidationException,
            NullTeamProfileException,
            CommanderValidationException,
            InvalidCommanderAssignmentException,
            RelationshipException
        ) as e:
            raise TeamValidationException(f"{method}: {TeamValidationException.DEFAULT_MESSAGE}") from e

        # This block catches any unexpected exceptions
        # You might want to log the error here before re-raising
        except Exception as e:
            raise TeamValidationException(f"An unexpected error occurred during validation: {e}") from e

#
# def main():
#
#     from chess.commander.commander import HumanCommander
#     person = HumanCommander(1, "person")
#
#     from chess.team import Team
#     team = Team(team_id=1, controller=person, profile=TeamProfile.BLACK)
#
#
# if __name__ == "__main__":
#     main()