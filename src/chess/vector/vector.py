# src/chess/vector/vector.py
"""
Module: chess.vector.vector
Author: Banji Lawal
Created: 2025-10-08

# SCOPE:
-------
***Limitation***: This module cannot prevent classes, processes or modules using `Vector`
    instances that pass sanity checks will not fail when using the validated `Vector`.
    Once client's processes might fail, experience service inconsistency or have other
    faults.
    Objects authenticated by `VectorValidator` might fail additional requirements
    a client has for a `Vector`. It is the client's responsibility to ensure the
    validated `Vector` passes and additional checks before deployment.

**Related Features**:
    `Coord` -> See `Coord`, `CoordBuilder`, `CoordValidator`, module[chess.visitor_coord],
    `Scalar` --> See `Scalar`, `ScalarValidator`, module[chess.vector],
    Handling process and rolling back failures --> See `Transaction`, module[chess.system]

# THEME:
-------
* Transform, geometry

# PURPOSE:
---------
1. Central, single source of truth for correctness of existing `Vector` objects.
2. Putting all the steps and logging into one place makes modules using `Vector` objects
    cleaner and easier to follow.

**Satisfies**: Consistency contracts.

# DEPENDENCIES:
---------------
From `chess.system`:
  * `LoggingLevelRouter`
From `chess.visitor_coord`:
  * `Coord`, `CoordValidator`, `KNIGHT_STEP_SIZE`, `LoggingLevelRouter`

From `chess.scalar`:
  * `Scalar`, `ScalarValidator`

from `chess.board_validator`
  * `SquareIterator`

From `chess.vector`:
    `Vector`, `NullVectorException`, `InvalidVectorException`, `NullXComponentException`,
    `NullYComponentException`, `VectorBelowBoundsException`, `VectorAboveBoundsException`

# CONTAINS:
----------
 * `VectorValidator`
"""


from chess.system import Result, LoggingLevelRouter
from chess.coord import Coord, CoordValidator
from chess.scalar import Scalar, ScalarValidator


class Vector:
  """
  # ROLE: Transformer

  # RESPONSIBILITY:
    Transforms `Coord`

  # PROVIDES:
  `Vector`

  # ATTRIBUTES:
    * `_x` (`int`): Amount added to `Coord.column`
    * `_y` (`int`): Amount added to `Coord.row`
  """
  _x: int
  _y: int

  def __init__(self, x: int, y: int):
    self._x = x
    self._y = y

  @property
  def x(self):
    return self._x

  @property
  def y(self):
    return self._y


  def __eq__(self, other):
    if other is self:
      return True
    if other is None:
      return False
    if not isinstance(other, Vector):
      return False
    return self._x == other.x and self._y == other.y


  def __hash__(self):
    return hash((self._x, self._y))


  @LoggingLevelRouter.monitor()
  def scalar_product(self, scalar: Scalar) -> Result['Vector']:
    """
    Action:
    Parameters:
      * `scalar` (`Scalar`): A scalar

    Returns:
      Result[`Vector`]

    Raises:
      `InvalidScalarException`
    """
    method = "Vector.scalar_product"

    try:
      validation = ScalarValidator.validate(scalar)
      if not validation.is_success():
        return Result(exception=validation.exception)

      return Result(payload=Vector(x=self._x  * scalar.value, y=self._y * scalar.value))
    except Exception as e:
      return Result(exception=e)


  @LoggingLevelRouter.monitor()
  def add_to_coord(self, coord: Coord) -> Result[Coord]:
    """
    Action:
      Transform a `Coord` by offsetting `Coord.row` and `Coord.column`.

    Parameters:
      * `visitor_coord` (`Coord`): A Coord object

    Returns:
      Result[`Coord`]

    Raises:
      `InvalidCoordException`
    """
    method = "Vector.add_to_coord"

    validation = CoordValidator.validate(coord)
    try:
      if not validation.is_success():
        return Result(exception=validation.exception)

      return Result(Coord(row=coord.row + self._y, column=coord.column + self._x))

    except Exception as e:
      return Result(exception=e)


  def __str__(self):
    return f"Vector(x={self._x}, y={self._y})"







  
