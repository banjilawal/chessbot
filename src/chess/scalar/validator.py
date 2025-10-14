from typing import cast, Generic, TypeVar

from chess.system import ValidationResult, Validator, BOARD_DIMENSION, LoggingLevelRouter, NullNumberException

from chess.scalar import (
  Scalar, NullScalarException, ScalarBelowBoundsException, ScalarAboveBoundsException, InvalidScalarException
)

T = TypeVar('T')

class ScalarValidator(Validator[Generic[T]]):
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

  @classmethod
  @LoggingLevelRouter.monitor
  def validate(cls, candidate: T) -> ValidationResult[Scalar]:
    """
    # ACTION:
    Verify the `candidate` is a valid ID. The Application requires
    1. Candidate is not null.
    2. Is a positive integer.

    # PARAMETERS:
        * `candidate` (`int`): the id.

    # RETURNS:
    `ValidationResult[str]`: A `ValidationResult` containing either:
        `'payload'` (`it`) - A `str` meeting the `ChessBot` standard for IDs.
        `exception` (`Exception`) - An exception detailing which naming rule was broken.

    # RAISES:
    `InvalidIdException`: Wraps any specification violations including:
        * `TypeError`: if candidate is not an `int`
        * `IdNullException`: if candidate is null
        * `NegativeIdException`: if candidate is negative `
    """
    """
    Validates that an existing `Scalar` instance meets specifications.
    This method performs team series of checks on team Scalar instance, ensuring it is not null and that
    its ID, name, and coordinate are valid. Exceptions from these checks are caught and re-raised
    as team `InvalidScalarException`, providing team clean and consistent err-handling experience.

    Args
      `candidate` (`Scalar`): `Scalar` instance to validate

     Returns:
      `Result`[`Scalar`]: A `Resul`candidate object containing the validated payload if the specification is satisfied,
      `InvalidScalarException` otherwise.

    Raises:
      `NullScalarException`: if `candidate` is null
      `TypeError`: if `candidate` is not Scalar
      `NullNumberException`: If `scalar.value` is null
      `ScalarBelowLowerBoundException`: If `scalar.value` < 0
      `ScalarAboveBoundsException`: If `scalar.value` >= `BOARD_DIMENSION`
      `InvalidScalarException`: Wraps any preceding exceptions
    """
    method = "ScalarValidator.validate"

    try:
      if candidate is None:
        return ValidationResult(exception=NullScalarException(f"{method} NullScalarException.DEFAULT_MESSAGE"))

      if not isinstance(candidate, Scalar):
        return ValidationResult(exception=TypeError(f"{method} Expected Scaler got `{type(candidate)}`"))


      scalar = cast(Scalar, candidate)

      if scalar.value is None:
        return ValidationResult(NullNumberException(f"{method} Scalar value cannot be a null number"))

      if scalar.value < -BOARD_DIMENSION:
        return ValidationResult(ScalarBelowBoundsException(
          f"{method}: {ScalarBelowBoundsException.DEFAULT_MESSAGE}"
          )
        )

      if scalar.value >= BOARD_DIMENSION:
        return ValidationResult(exception=ScalarAboveBoundsException(
          f"{method}: {ScalarAboveBoundsException.DEFAULT_MESSAGE}"
          )
        )

      return ValidationResult(payload=scalar)

    except Exception as e:
      return ValidationResult(InvalidScalarException(f"{method}: {e}"))
    # This block catches any unexpected exceptions
    # You might want to log the error here before re-raising


# def main():
#   result = ScalarSpecification.is_satisfied_by(Scalar(3))
#   if result.is_success():
#     print(f"Scalar is valid: {result.payload}")
#   else:
#     print(f"Scalar is invalid: {result.team_exception}")
#
# if __name__ == "__main__":
#   main()