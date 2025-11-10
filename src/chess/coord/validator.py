from typing import cast, TypeVar

from chess.system import Validator, ValidationResult, LoggingLevelRouter, ROW_SIZE, COLUMN_SIZE
from chess.coord import (
  Coord, NullCoordException, NullRowException, RowBelowBoundsException, RowAboveBoundsException, NullColumnException,
  ColumnBelowBoundsException, ColumnAboveBoundsException, InvalidCoordException
)


T = TypeVar('T')

class CoordValidator(Validator[Coord]):
  """
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
        * `candidate` (`int`): the visitor_id.

    # RETURNS:
    `ValidationResult[str]`: A `ValidationResult` containing either:
        `'payload'` (`it`) - A `str` meeting the `ChessBot` standard for IDs.
        `rollback_exception` (`Exception`) - An rollback_exception detailing which naming rule was broken.

    # RAISES:
    `InvalidIdException`: Wraps any specification violations including:
        * `TypeError`: if candidate is not an `int`
        * `IdNullException`: if candidate is null
        * `NegativeIdException`: if candidate is negative `
    """


    method = "CoordValidator.validate"
    try:
      """
      Tests are chained in this specific order for team_name reason.
      """

      # If candidate is null no point continuing
      if candidate is None:
        return ValidationResult(exception=NullCoordException(f"{method} NullCoordException.DEFAULT_MESSAGE"))

      # If cannot cast from candidate to Coord need to break
      if not isinstance(candidate, Coord):
        return ValidationResult(exception=TypeError(f"{method} Expected team_name Coord, got {type(candidate).__name__}"))

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

      # Return the notification if checks passed
      return ValidationResult(payload=coordinate)

    except Exception as e:
      return ValidationResult(exception=InvalidCoordException(f"{method}: {e}"))