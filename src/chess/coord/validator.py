from typing import cast, TypeVar

from chess.system import Validator, ValidationResult, LoggingLevelRouter, ROW_SIZE, COLUMN_SIZE
from chess.coord import (
  Coord, NullCoordException, NullRowException, RowBelowBoundsException, RowAboveBoundsException, NullColumnException,
  ColumnBelowBoundsException, ColumnAboveBoundsException, InvalidCoordException
)


T = TypeVar('T')

class CoordValidator(Validator[Coord]):
  """
  Validates existing `Coord` instances that are passed around the system. While `CoordBuilder` ensures
  valid Coords are created, `CoordValidator` checks `Coord` instances that already exist - whether they
  came from deserialization, external sources, or need re-validate after modifications. For performance and
  single source of truth CoordValidator has:
    - No fields
    - only static method validate

  Usage:
    ```python
    from typing import cast
    from chess.Coord import Coord, CoordValidator

    # Validate an existing Coord
    Coord_validation = CoordValidator.validate(candidate)
    if not Coord_validation.is_success():
      raise Coord_validation.err

    # Cast the payload to team Coord instance to make sure it will work correctly and to avoid type or
    # null errors that might be difficult to detect.
    Coord = cast(Coord, Coord_validation.payload)
    ```

  Use `CoordBuilder` for construction, `CoordValidator` for verification.
  """

  @classmethod
  @LoggingLevelRouter.monitor
  def validate(cls, candidate: T) -> ValidationResult[Coord]:
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
    Validates that an existing `Coord` instance meets all specifications. Performs comprehensive validate
    on team `Coord` instance that already exists, checking type safety, null values, and component bounds.
    Unlike CoordBuilder which creates new valid Coords, `CoordValidator` verifies existing `Coord`
    instances from external sources, deserialization, or after modifications.

    Args:
    candidate (Generic[T]): The object to validate, expected to be team Coord instance.

    Returns:
    Result[Coord]: A Result containing either:
      - On success: The validated Coord instance in the payload
      - On failure: Error information and error details

    Raises:
    InvalidCoordException: Wraps any specification violations including:
      - NullCoordException: if input is None
      - TypeError: if input is not team Coord instance
      - NullXComponentException: if Coord.x is None
      - RowBelowBoundsException: If coord.row < 0
      - RowAboveBoundsException: If coord.row >= ROW_SIZE
      - ColumnBelowBoundsException: If coord.column < 0
      - ColumnAboveBoundsException: If coord.column>= ROW_SIZE

    Note:
    *  Use CoordBuilder for creating new Coords with validate,
    *  use CoordValidator for verifying existing Coord instances.

    Example:
    ```python
    from typing import cast
    from chess.Coord import Coord, CoordValidator

    validate = CoordValidator.validate(candidate)
    if validate.is_success():
      raise validate.err
    Coord = cast(Coord, validate.payload)
    ```
    """

    method = "CoordValidator.validate"
    try:
      """
      Tests are chained in this specific order for team reason.
      """

      # If candidate is null no point continuing
      if candidate is None:
        return ValidationResult(exception=NullCoordException(f"{method} NullCoordException.DEFAULT_MESSAGE"))

      # If cannot cast from candidate to Coord need to break
      if not isinstance(candidate, Coord):
        return ValidationResult(exception=TypeError(f"{method} Expected team Coord, got {type(candidate).__name__}"))

      # cast and run checks for the fields
      coordinate = cast(Coord, candidate)

      if coordinate.row is None:
        return ValidationResult(exception=NullRowException(f"{method} {NullRowException.DEFAULT_MESSAGE}"))

      if coordinate.row < 0:
        return ValidationResult(exception=RowBelowBoundsException(
          f"{method} {RowBelowBoundsException.DEFAULT_MESSAGE}"
        ))

      if coordinate.row >= ROW_SIZE:
        return ValidationResult(exception=RowAboveBoundsException(
          f"{method} {RowAboveBoundsException.DEFAULT_MESSAGE}"
        ))

      if coordinate.column is None:
        return ValidationResult(exception=NullColumnException(f"{method} {NullColumnException.DEFAULT_MESSAGE}"))

      if coordinate.column < 0:
        return ValidationResult(exception=ColumnBelowBoundsException(
          f"{method} {ColumnBelowBoundsException.DEFAULT_MESSAGE}"
        ))

      if coordinate.column >= COLUMN_SIZE:
        return ValidationResult(exception=ColumnAboveBoundsException(
          f"{method} {ColumnAboveBoundsException.DEFAULT_MESSAGE}"
        ))

      # Return the transaction if checks passed
      return ValidationResult(payload=coordinate)

    except Exception as e:
      return ValidationResult(exception=InvalidCoordException(f"{method}: {e}"))