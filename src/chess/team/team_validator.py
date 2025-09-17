from typing import cast, Generic, TYPE_CHECKING

from assurance.exception.invalid_id import IdValidationException
from chess.team.team_exception.invalid_team import TeamValidationException
from chess.commander.exception.invalid_commander import CommanderValidationException
from chess.competitor.commander import Commander

from chess.team.team_profile import TeamProfile
from chess.team.team_exception.null_team_profile import NullTeamProfileException

from chess.team.team_exception.null_team import NullTeamException
from chess.result import Result
from chess.common.validator import Validator, T
from chess.common.id.validator import IdValidator
from chess.exception.stack_exception import BrokenRelationshipException

if TYPE_CHECKING:
    from chess.side.team import Side


class TeamValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result['Team']:
        entity = "Team"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates a team with chained exceptions for team meeting specifications:
            - Not null
            - id passes validator checks
            - commander passes validator checks
        An unmet requirements raise an team_exception which encapsulated in a TeamValidationException

        Args
            t (Team): team to validate

         Returns:
             Result[T]: A Result object containing the validated payload if the specification is satisfied,
            TeamValidationException otherwise.

        Raises:
            TypeError: if t is not Team
            NullTeamException: if t is null   

            IdValidationException: if invalid id
            CommanderValidationException: if invalid commander

            TeamValidationException: Wraps any preceding exceptions      
        """
        try:
            if t is None:
                raise NullTeamException(f"{method} {NullTeamException.DEFAULT_MESSAGE}")

            from chess.side.team import Side
            if not isinstance(t, Side):
                raise TypeError(f"{method} Expected a Team, got {type(t).__name__}")

            side = cast(Side, t)

            if side.profile is None:
                raise NullTeamProfileException(f"{method}: {NullTeamProfileException.DEFAULT_MESSAGE}")

            id_validation = IdValidator.validate(side.id)
            if not id_validation.is_success():
                raise IdValidationException(f"{method}: {IdValidationException.DEFAULT_MESSAGE}")

            from chess.commander.commander_validator import CommanderValidator
            competitor_validation = CommanderValidator.validate(side.commander)
            if not competitor_validation.is_success():
                raise CommanderValidationException(
                    f"{method}: {CommanderValidationException.DEFAULT_MESSAGE}"
                )
            competitor = cast(Commander, competitor_validation.payload)

            if side not in competitor.teams.items:

                raise BrokenRelationshipException(f"{method}: {BrokenRelationshipException.DEFAULT_MESSAGE}")

            return Result(payload=side)

        except (
                TypeError,
                NullTeamException,
                IdValidationException,
                NullTeamProfileException,
                CommanderValidationException
        ) as e:
            raise TeamValidationException(f"{method}: {TeamValidationException.DEFAULT_MESSAGE}") from e



def main():

    from chess.competitor.commander import HumanCommander
    person = HumanCommander(1, "person")

    from chess.side.team import Side
    side = Side(side_id=1, controller=person, profile=TeamProfile.BLACK)


if __name__ == "__main__":
    main()