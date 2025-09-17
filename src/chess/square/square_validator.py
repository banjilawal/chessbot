from typing import cast, Generic, TypeVar

from chess.common import Result, Validator
from chess.coord import CoordValidator, CoordValidationException
from chess.square import Square, NullSquareException, SquareValidationException
from assurance import IdValidator, NameValidator, IdValidationException, NameValidationException

T = TypeVar('T')

class SquareValidator(Validator):
    @staticmethod
    def validate(t: Generic[T]) -> Result[Square]:
        method = "SquareValidator.validate"

        """Validates a Square object.

        This method performs a series of checks on a Square instance, ensuring it is not null and that 
        its ID, name, and coordinate are valid. Exceptions from these checks are caught and re-raised 
        as a SquareValidationException, providing a clean and consistent error-handling experience.

        Args:
            t (Square): The square object to validate.

        Returns:
            Result[Square]: A Result object containing the validated Square if all specifications are met.

        Raises:
            TypeError: If the input `t` is not an instance of `Square`.
            NullSquareException: If the input `t` is `None`.
            SquareValidationException: If the square fails any internal validation checks. This 
                team_exception wraps the original validation-specific team_exception (e.g., `IdValidationException`).
        """
        try:
            if t is None:
                raise NullSquareException("Square reference cannot be null.")

            if not isinstance(t, Square):
                raise TypeError(f"Expected a Square, but got {type(t).__name__}.")

            square = cast(Square, t)

            id_result = IdValidator.validate(square.id)
            if not id_result.is_success():
                raise id_result.exception

            name_result = NameValidator.validate(square.name)
            if not name_result.is_success():
                raise name_result.exception

            coord_result = CoordValidator.validate(square.coord)
            if not coord_result.is_success():
                raise coord_result.exception

            return Result(payload=square)

        except (
            TypeError,
            NullSquareException,
            IdValidationException,
            NameValidationException,
            CoordValidationException
        ) as e:
            raise SquareValidationException("Square failed validation.") from e

        # This block catches any unexpected exceptions
        # You might want to log the error here before re-raising
        except Exception as e:
            raise SquareValidationException(f"An unexpected error occurred during validation: {e}") from e
