from typing import cast, Generic, TYPE_CHECKING

from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.team import SideValidationException
from assurance.exception.validation.competitor import CompetitorValidationException
from chess.competitor.commander import Commander

from chess.config.game import SideProfile
from chess.exception.null.side_profile import NullSideProfileException

from chess.exception.null.side import NullSideException
from chess.result import Result
from chess.common.validator import Validator, T
from assurance.validators.id import IdValidator
from chess.exception.stack import BrokenRelationshipException

if TYPE_CHECKING:
    from chess.side.team import Side


class SideValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result['Side']:
        entity = "Side"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates a team with chained exceptions for team meeting specifications:
            - Not null
            - id passes validator checks
            - commander passes validator checks
        An unmet requirements raise an exception which encapsulated in a SideValidationException

        Args
            t (Side): team to validate

         Returns:
             Result[T]: A Result object containing the validated payload if the specification is satisfied,
            SideValidationException otherwise.

        Raises:
            TypeError: if t is not Side
            NullSideException: if t is null   

            IdValidationException: if invalid id
            CompetitorValidationException: if invalid commander

            SideValidationException: Wraps any preceding exceptions      
        """
        try:
            if t is None:
                raise NullSideException(f"{method} {NullSideException.DEFAULT_MESSAGE}")

            from chess.side.team import Side
            if not isinstance(t, Side):
                raise TypeError(f"{method} Expected a Side, got {type(t).__name__}")

            side = cast(Side, t)

            if side.profile is None:
                raise NullSideProfileException(f"{method}: {NullSideProfileException.DEFAULT_MESSAGE}")

            id_validation = IdValidator.validate(side.id)
            if not id_validation.is_success():
                raise IdValidationException(f"{method}: {IdValidationException.DEFAULT_MESSAGE}")

            from assurance.validators.competitor import CompetitorValidator
            competitor_validation = CompetitorValidator.validate(side.controller)
            if not competitor_validation.is_success():
                raise CompetitorValidationException(
                    f"{method}: {CompetitorValidationException.DEFAULT_MESSAGE}"
                )
            competitor = cast(Commander, competitor_validation.payload)

            if side not in competitor.sides_played.items:

                raise BrokenRelationshipException(f"{method}: {BrokenRelationshipException.DEFAULT_MESSAGE}")

            return Result(payload=side)

        except (
            TypeError,
            NullSideException,
            IdValidationException,
            NullSideProfileException,
            CompetitorValidationException
        ) as e:
            raise SideValidationException(f"{method}: {SideValidationException.DEFAULT_MESSAGE}") from e



def main():

    from chess.competitor.commander import HumanCommander
    person = HumanCommander(1, "person")

    from chess.side.team import Side
    side = Side(side_id=1, controller=person, profile=SideProfile.BLACK)


if __name__ == "__main__":
    main()