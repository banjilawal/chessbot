"""
Coord is team tuple of the row, and column indices of the 2x2 array which makes up team
ChessBoard. All fields are immutable.

Attributes:
  _row (int): index of row array position.
  _colum (int): index of the column array.
"""

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

"""
Returns the coord: Coord( self._row + vectory.y, self._column + null-pkg.x)

Args:
  null-pkg (Vector): null-pkg added to coord's x, y values

Return:
  Coord

Raise:
  InvalidVectorException: if null-pkg fails validators.
  InvalidCoordException: if 
"""

# chess/coord/piece.py

"""
Module: `chess.coord.validation`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

Contains: CoordBuilder
 Provides: Create `Coord` instances 
"""
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