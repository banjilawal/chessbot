from typing import cast, Generic


from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.owner import OwnerValidationException

from assurance.exception.validation.team import TeamValidationException
from assurance.result.base import Result
from assurance.validators.base import Validator, T
from assurance.validators.id import IdValidator
from assurance.validators.owner import CompertitorValidator

from chess.exception.null.team import NullTeamException
from chess.team.model import Side


class TeamValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[Side]:
        entity = "Team"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates a team with chained exceptions for team meeting specifications:
            - Not null
            - id passes validation checks
            - competitor passes validation checks
        An unmet requirements raise an exception which encapsulated in a TeamValidationException

        Args
            t (Team): team to validate

         Returns:
             Result[T]: A Result object containing the validated payload if the specification is satisfied,
            TeamValidationException otherwise.

        Raises:
            TypeError: if t is not Team
            NullTeamException: if t is null   

            IdValidationException: if invalid id
            OwnerValidationException: if invalid competitor

            TeamValidationException: Wraps any preceding exceptions      
        """
        try:
            if t is None:
                raise NullTeamException(f"{method} {NullTeamException.DEFAULT_MESSAGE}")

            if not isinstance(t, Side):
                raise TypeError(f"{method} Expected a Team, got {type(t).__name__}")

            team = cast(Side, t)

            id_validation = IdValidator.validate(team.id)
            if not id_validation.is_success():
                raise IdValidationException(f"{method}: {IdValidationException.DEFAULT_MESSAGE}")

            owner_validation = CompertitorValidator.validate(team.controller)
            if not owner_validation.is_success():
                raise OwnerValidationException(f"{method}: {OwnerValidationException.DEFAULT_MESSAGE}")

            return Result(payload=team)

        except (
            TypeError,
            NullTeamException,
            IdValidationException,
            OwnerValidationException
        ) as e:
            raise TeamValidationException(f"{method}: {TeamValidationException.DEFAULT_MESSAGE}") from e