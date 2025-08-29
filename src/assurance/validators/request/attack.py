
from assurance.exception.validation.request.base import RequestValidationException


class AttackRequestValidationException(RequestValidationException):
    ERROR_CODE = "ATTACK_REQUEST_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"AttackRequest validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
class PieceValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[Piece]:
        entity = "Piece"
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
            PieceValidationException,
            SquareValidationException,
            NullAttackRequestException
        ) as e:
            raise AttackRequestValidationException(
                f"{method}: {AttackRequestValidationException.DEFAULT_MESSAGE}"
            ) from e