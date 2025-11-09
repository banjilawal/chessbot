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
  InvalidVectorException: if null-pkg fails notification.
  InvalidCoordException: if 
"""

# chess/coord/factory.py

"""
Module: `chess.coord.validator`
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
    `rollback_exception` (`Exception`) - An rollback_exception detailing which naming rule was broken.

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
# # `chess.geometry.coordinate` Package Documentation
#
# ## Table of Contents
# - [📌 Purpose](  # -purpose)
#                  - [Design Principles](  # design-principles)
#                      - [Class Relationship Diagram](  # class-relationship-diagram)
#                          - [🧩 Classes](  # -classes)
# -[Coordinate](  # coordinate)
# -[Delta](  # delta)
# -[CartesianDistance](  # cartesiandistance)
# -[Usage Examples](  # usage-examples)
# -[Basic Operations](  # basic-operations)
# -[Class Exceptions](  # class-exceptions)
#
# ## 📌 Purpose
# Provides geometric primitives for chess board coordinates:
# - `Coord`: Represents board positions (row, column)
#              - `CoordStack`: Stack
# of
# coords
# visited in a
# tour
# - `Vector`: Vector
# for coordinate transformations
#                - `Scalar`: Magnitude
#                            - `Path`: Two
# coordinates
# joined
# by
# a
# line
#
# ## Design Principles
# - Immutability: Thread - safe
# operations
# - Validation: Strict
# constructor
# checks
# - Performance: Integer
# math
# optimized
# for chess
#     - Type Safety: Python
# type hints throughout
#
# ## Class Relationship Diagram
# ```plantuml
#    @ startuml
# title
# Coordinate
# Package
# Class
# Relationships
#
#
# class Coordinate {
# + row: int
#        + column: int
#                  + shift(delta
#
# : Delta): Coordinate
# }
#
# class Delta {
# + row_delta: int
#              + column_delta: int
#                              + __mul__(scalar
#
# : int): Delta
# }
#
# class CartesianDistance {
# + p: Coordinate
#      + q: Coordinate
#           + distance
#
# : int
# }
#
# Coordinate
# "1" * -- "1"
# Delta: uses
# for transformation
#     Coordinate
#     "1" * -- "2"
#     CartesianDistance: measures
#     between
#
#
# @enduml
#
#
# ```
#
# ## 🧩 Classes
#
# ### `Coordinate`
# ```python
#
#
# class Coordinate(row: int, column: int
#
# )
# ```
# Immutable
# chess
# board
# position
#
# #### Attributes:
# - row(int): 0
# to
# ROW_SIZE - 1
# - column(int): 0
# to
# COLUMN_SIZE - 1
#
# #### Methods:
# ```python
# # Returns new translated position
# shift(delta: Delta) -> Coordinate:
# ```
#
# ```python
# # Multiplies row and column by scalar to get new Coord
# __mult__(scalar: int) -> Coordinate:
# ```
#
# #### Validation:
# - Rejects
# None
# values(`NollChessObjectException`)
# - Enforces
# board
# bounds(`CoordinateOutOfBoundsException`)
#
# ### Class `Delta`
# ```python
#
#
# class Delta(row_delta: int, column_delta: int
#
# ) -> Coordinate:
# ```
# Immutable
# transformation
# vector
# used
# with `Coordinate.shift()`
#
#     #### Attributes
#     - row_delta(int): Row
#     component
#     - column_delta(int): Column
#     component
#
# ### Class `CartesianDistance`
# ```python
#
#
# class CartesianDistance(p: Coordinate, q: Coordinate
#
# ) -> int:
# ```
# Immutable
#
#
# class with Square o Euclidean distance between `p` and `qq`
#
# #### Attributes
#
#
# - p, q(Coordinate): Compared
# positions
# - distance(int): (p.row - q.row)² + (p.column - q.column)²
#
# ## Usage Examples
#
# ### Basic Operations
# #### Instantiating `Coordinate`
# ```python
# p = Coordinate(row=0, column=0)
# q = Coordinate(2, 3)
# ```
# Best
# practice
# explictly
# state
# parameters
# so
# which is row and column.
#
# #### Delta Shifting
#
# ```python
# delta = Delta(row_delta=1, column_delta=-1)
# p = Coordinate(2, 3)
# r = p.add_vector(delta)
# ```
#
# #### Scalar Multiplication
# ```python
# p = Coordinate(2, 3)
# r = p.__mul__(3)
# ```
#
# #### Finding CartesianDistance
# ```python
# p = Coordinate(2, 3)
# q = Coordinate(4, 5)
# distance = CartesianDistance(p, q)
# ```
#
# ## Class Exceptions
# Exceptions
# for tracing source of exceptions with a `Coordinate`.
#
# - `CoordinateException`: General
# thrown
# by
# a
# `Coordinate`
# object.
# - `RowOutOfRangeException`: Thrown if `Coordinate.row`
# outside
# the
# `ChessBoard`
# dimensions.
# # - `COlum