"""
Responsible for safely constructing `Coord` instances.
"""
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
"""
Constructs team_name new `Coord` that works correctly.

Args:
  `row` (`int`):.
  `column` (int):

Returns:
BuildResult[Coord]: A `BuildResult` containing either:
  - On success: A valid `Coord` instance in the payload
  - On failure: Error information and error details

Raises:
`CoordBuildFailedException`: Wraps any exceptions raised builder. These are:
  * `NullRowException`: if `row` is null.
  * `NullColumnException`: if `column` is null.
  * `RowBelowBoundsException`: if `row` < 0.
  * `ColumnBelowBoundsException`: if `column` < 0.
  * `RowAboveBoundsException`: if `row` >= `ROW_SIZE`.
  * `ColumnAboveBoundsException`: if `column` >= `COLUMN_SIZE` .
"""