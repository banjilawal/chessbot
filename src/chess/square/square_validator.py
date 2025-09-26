from typing import cast, Generic, TypeVar


from chess.coord import CoordValidator, CoordValidationException
from chess.square import Square, NullSquareException, SquareValidationException
from chess.common import Result, Validator, IdValidator, NameValidator, IdValidationException, NameValidationException


T = TypeVar('T')

class SquareValidator(Validator):
    """
    Validates existing `Square` instances that are passed around the system.

    While `SquareBuilder` ensures valid Squares are created, `SquareValidator`
    checks `Square` instances that already exist - whether they came from
    deserialization, external sources, or need re-validation after modifications.

    Usage:
        ```python
        # Validate an existing square
        square_validation = SquareValidator.validate(candidate)
        if not square_validation.is_success():
            raise square_validation.exception
        square = cast(Square, square_validation.payload)
        ```

    Use `SquareBuilder` for construction, `SquareValidator` for verification.
    """
    
    @staticmethod
    def validate(t: Generic[T]) -> Result[Square]:
        """
        Validates that an existing `Square` instance meets specifications.
        This method performs a series of checks on a Square instance, ensuring it is not null and that 
        its ID, name, and coordinate are valid. Exceptions from these checks are caught and re-raised 
        as a `SquareValidationException`, providing a clean and consistent error-handling experience.

        Args
            `t` (`Square`): `Square` instance to validate

         Returns:
            `Result`[`Square`]: A `Resul`t object containing the validated payload if the specification is satisfied,
            `SquareValidationException` otherwise.

        Raises:
            `TypeError`: If the input `t` is not an instance of `Square`.
            `NullSquareException`: If the input `t` is `None`.
            `IdValidationException`: If the `id` attribute of the square fails validation checks.
            `NameValidationException`: If the `name` attribute of the square fails validation checks.
            `CoordValidationException`: If the `coord` attribute of the square fails validation checks.
            `SquareValidationException`: Wraps any preceding exceptions
        """
        method = "SquareValidator.validate"
        
        try:
            if t is None:
                raise NullSquareException(f"{method} {NullSquareException.DEFAULT_MESSAGE}")

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
