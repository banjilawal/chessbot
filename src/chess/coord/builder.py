# chess/coord/validation.py

"""
Module: `chess.coord.validation`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

Contains: CoordBuilder
 Provides: Create `Coord` instances 
"""

from chess.system import Builder, ROW_SIZE, COLUMN_SIZE, BuildResult, LoggingLevelRouter, LoggingLevelRouter
from chess.coord import (
  Coord,
  NullRowException,
  NullColumnException,
  RowBelowBoundsException,
  RowAboveBoundsException,
  ColumnBelowBoundsException,
  ColumnAboveBoundsException,
  CoordBuildFailedException
)

class CoordBuilder(Builder[Coord]):
  """
  Responsible for safely constructing `Coord` instances.
  """

  @classmethod
  def build(cls, row: int, column: int) -> BuildResult[Coord]:
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
    Constructs team new `Coord` that works correctly.

    Args:
      `row` (`int`):.
      `column` (int):

    Returns:
    BuildResult[Coord]: A `BuildResult` containing either:
      - On success: A valid `Coord` instance in the payload
      - On failure: Error information and error details

    Raises:
    `CoordBuildFailedException`: Wraps any exceptions raised build. These are:
      * `NullRowException`: if `row` is null.
      * `NullColumnException`: if `column` is null.
      * `RowBelowBoundsException`: if `row` < 0.
      * `ColumnBelowBoundsException`: if `column` < 0.
      * `RowAboveBoundsException`: if `row` >= `ROW_SIZE`.
      * `ColumnAboveBoundsException`: if `column` >= `COLUMN_SIZE` .
    """
    method = "CoordBuilder.build"

    try:
      if row is None:
        LoggingLevelRouter.log_and_raise_error(
          CoordBuilder,
          NullRowException(f"{method} {NullRowException.DEFAULT_MESSAGE}")
        )
      if row < 0:
        LoggingLevelRouter.log_and_raise_error(
          CoordBuilder,
          RowBelowBoundsException(f"{method} {RowBelowBoundsException.DEFAULT_MESSAGE}")
        )
      if row >= ROW_SIZE:
        LoggingLevelRouter.log_and_raise_error(
          CoordBuilder,
          RowAboveBoundsException(f"{method} {RowAboveBoundsException.DEFAULT_MESSAGE}")
        )

      if column is None:
        LoggingLevelRouter.log_and_raise_error(
          CoordBuilder,
          NullColumnException(f"{method} {NullRowException.DEFAULT_MESSAGE}")
        )
      if column < 0:
        LoggingLevelRouter.log_and_raise_error(
          CoordBuilder,
          ColumnBelowBoundsException(f"{method} {ColumnBelowBoundsException.DEFAULT_MESSAGE}")
        )
      if column >= COLUMN_SIZE:
        LoggingLevelRouter.log_and_raise_error(
          CoordBuilder,
          ColumnAboveBoundsException(f"{method} {ColumnAboveBoundsException.DEFAULT_MESSAGE}")
        )
      return BuildResult(payload=Coord(row=row, column=column))

    except (
      NullRowException,
      NullColumnException,
      RowBelowBoundsException,
      ColumnBelowBoundsException,
      RowAboveBoundsException,
      ColumnAboveBoundsException,
    ) as e:
      raise CoordBuildFailedException(f"{method}: {e}") from e

    # Catch any unexpected errors with details about type and message
    except Exception as e:
      raise CoordBuildFailedException(
        f"{method}: Unexpected error ({type(e).__name__}): {e}"
      ) from e
