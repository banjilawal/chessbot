from crypt import methods
from typing import cast, Generic, TYPE_CHECKING, TypeVar

from chess.common import Result, Validator, IdValidator, IdValidationException
from chess.search import CommanderSearch
from chess.exception import BrokenRelationshipException
from chess.team import Team, NullTeamException, NullTeamProfileException, TeamValidationException
from chess.commander import Commander, CommanderValidator, CommanderValidationException

T = TypeVar('T')

class TeamValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result['Team']:
        """
         Validates that an existing Team instance meets specifications:
            - Not null
            - `id` passes validator checks
            - `commander` passes validator checks

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
            `BrokenRelationshipException`: if the bidirectional relationship between Team and Commander is broken
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
            CommanderSearch.for_team(team.id, commander)

            if team not in commander.teams.items:
                raise BrokenRelationshipException(f"{method}: {BrokenRelationshipException.DEFAULT_MESSAGE}")

            return Result(payload=team)

        except (
            TypeError,
            NullTeamException,
            IdValidationException,
            NullTeamProfileException,
            CommanderValidationException
        ) as e:
            raise TeamValidationException(f"{method}: {TeamValidationException.DEFAULT_MESSAGE}") from e


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