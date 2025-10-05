from typing import cast, Generic, TypeVar

from chess.exception import NullNumberException
from chess.system import Result, Validator, BOARD_DIMENSION

from chess.scalar import(
  Scalar, NullScalarException, ScalarBelowBoundsException,
  ScalarAboveBoundsException, InvalidScalarException
)

T = TypeVar('T')

class ScalarValidator(Validator):
  """
  Validates existing `Scalar` instances that are passed around the system.

  While `ScalarBuilder` ensures valid Scalars are created, `ScalarValidator`
  checks `Scalar` instances that already exist - whether they came from
  deserialization, external sources, or need re-validate after modifications.

  Usage:
    ```python
    # Validate an existing scalar
    scalar_validation = ScalarValidator.validate(candidate)
    if not scalar_validation.is_success():
      raise scalar_validation.err
    scalar = cast(Scalar, scalar_validation.payload)
    ```

  Use `ScalarBuilder` for construction, `ScalarValidator` for verification.
  """

  @staticmethod
  def validate(t: Scalar) -> Result[Scalar]:
    """
    Validates that an existing `Scalar` instance meets specifications.
    This method performs a series of checks on a Scalar instance, ensuring it is not null and that
    its ID, name, and coordinate are valid. Exceptions from these checks are caught and re-raised
    as a `InvalidScalarException`, providing a clean and consistent err-handling experience.

    Args
      `t` (`Scalar`): `Scalar` instance to validate

     Returns:
      `Result`[`Scalar`]: A `Resul`t object containing the validated payload if the specification is satisfied,
      `InvalidScalarException` otherwise.

    Raises:
      `NullScalarException`: if `t` is null
      `TypeError`: if `t` is not Scalar
      `NullNumberException`: If `scalar.value` is null
      `ScalarBelowLowerBoundException`: If `scalar.value` < 0
      `ScalarAboveBoundsException`: If `scalar.value` >= `BOARD_DIMENSION`
      `InvalidScalarException`: Wraps any preceding exceptions
    """
    method = "ScalarValidator.validate"

    try:
      if t is None:
        raise NullScalarException(f"{method} NullScalarException.DEFAULT_MESSAGE")


      scalar = cast(Scalar, t)

      if scalar.value is None:
        raise NullNumberException(f"{method} {NullNumberException.DEFAULT_MESSAGE}")

      if scalar.value < -BOARD_DIMENSION:
        raise ScalarBelowBoundsException(
          f"{method}: {ScalarBelowBoundsException.DEFAULT_MESSAGE}"
        )

      if scalar.value >= BOARD_DIMENSION:
        raise ScalarAboveBoundsException(
          f"{method}: {ScalarAboveBoundsException.DEFAULT_MESSAGE}"
        )

      return Result(payload=scalar)

    except (
      TypeError,
      NullScalarException,
      NullNumberException,
      ScalarBelowBoundsException,
      ScalarAboveBoundsException,
    ) as e:
      raise InvalidScalarException(f"{method}: {InvalidScalarException.DEFAULT_MESSAGE}") from e

    # This block catches any unexpected exceptions
    # You might want to log the error here before re-raising
    except Exception as e:
      raise InvalidScalarException(f"An unexpected error occurred during validate: {e}") from e


# def main():
#   result = ScalarSpecification.is_satisfied_by(Scalar(3))
#   if result.is_success():
#     print(f"Scalar is valid: {result.payload}")
#   else:
#     print(f"Scalar is invalid: {result.team_exception}")
#
# if __name__ == "__main__":
#   main()