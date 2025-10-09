# src/chess/piece/event/transaction
"""
Module: chess.piece.event.transaction
Author: Banji Lawal
Created: 2025-09-28

# SCOPE:
* The limits of the module, defined by what it does not do.
* Where to look for related features this models does not provide because of its limitations.

# THEME:
* Highlight the core feature (thread-safety)
* Explain the how-and-why of implementation choices.

# PURPOSE:
* Function and role in the system.
* Why the module exists in the application architecture
* What problem it fundamentally solves

# DEPENDENCIES:

# CONTAINS:
 * ``
"""


from chess.system import Result
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

  def add_to_coord(self, coord: Coord) -> Result[Coord]:
    """
    Action:
      Transform a `Coord` by offsetting r
    Parameters:
      * `coord` (`Coord`): A Coord object

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







  
