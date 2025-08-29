from typing import cast, Generic

from assurance.exception.validation.coord import CoordinateValidationException
from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.name import NameValidationException
from assurance.exception.validation.square import SquareValidationException
from assurance.result.base import Result
from assurance.validators.base import Validator, T
from assurance.validators.coord import CoordinateValidator
from assurance.validators.id import IdValidator
from assurance.validators.name import NameValidator
from chess.board.square import Square
from chess.exception.null.square import NullSquareException
from chess.team.model import Team


class TeamValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[Team]:
        entity = "Team"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates a square with chained exceptions for square meeting specifications:
            - Not null
            - id fails validation
            - name fails validation
            - coordinate fails validation
        If validators fails their exception will be encapsulated in a SquareValidationException

        Args
            t (Square): square to validate

         Returns:
             Result[T]: A Result object containing the validated payload if the specification is satisfied,
                SquareValidationException otherwise.

        Raises:
            TypeError: if t is not Square
            NullSquareException: if t is null   

            IdValidationException: if invalid id
            NameValidationException: if invalid name
            CoordinateValidationException: if invalid coordinate

            SquareValidationException: Wraps any preceding exceptions      
        """
        try:
            if t is None:
                raise NullSquareException(
                    f"{method} {NullSquareException.DEFAULT_MESSAGE}"
                )

            if not isinstance(t, Square):
                raise TypeError(f"{method} Expected a Square, got {type(t).__name__}")

            square = cast(Square, t)

            id_result = IdValidator.validate(square.id)
            if not id_result.is_success():
                raise IdValidationException(
                    f"{method}: {IdValidationException.DEFAULT_MESSAGE}"
                )

            name_result = NameValidator.validate(square.name)
            if not name_result.is_success():
                raise NameValidationException(
                    f"{method}: {NameValidationException.DEFAULT_MESSAGE}"
                )

            coord_result = CoordinateValidator.validate(square.coordinate)
            if not coord_result.is_success():
                raise CoordinateValidationException(
                    f"{method}: {CoordinateValidationException.DEFAULT_MESSAGE}"
                )

            return Result(payload=square)

        except (
            TypeError,
            NullSquareException,
            IdValidationException,
            NameValidationException,
            CoordinateValidationException
        ) as e:
            raise SquareValidationException(
                f"{method}: {SquareValidationException.DEFAULT_MESSAGE}"
            ) from e