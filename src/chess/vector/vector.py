
from chess.system import KNIGHT_STEP_SIZE
from chess.vector import (
  NullXComponentException, NullYComponentException,
  VectorAboveBoundsException, VectorBelowBoundsException
)

from chess.scalar import Scalar

class Vector:
  _x: int
  _y: int

  """
  Offset is an immutable class is used for shifting a Coord by a null-pkg. The Offset is just a null-pkg 
  added to a Coord null-pkg. Moved responsibility for coordinate_vector algebra from Vector to Coord, the 
  testing and verification is simpler. This leaves Vector a pure data class used for transforming a Coord.

  Attributes:
    _x (int): Amount added to target coord's row
    _y (int): Amount added to target coord's column
  """

  def __init__(self, x: int, y: int):
    method = f"Offset__init__"

    """
    Constructs a Offset instance.
    
    Args:
      delta_row (int): value for _delta_row
      delta_column (int): value fpr delta_column
      
    Raises:
      NollChessObjectException: if either delta_row or delta_column are null.
    """

    if x is None:
      raise NullXComponentException(f"{method}: {NullXComponentException.DEFAULT_MESSAGE}")

    if x < -KNIGHT_STEP_SIZE or y < KNIGHT_STEP_SIZE:
      raise VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}")

    if x > KNIGHT_STEP_SIZE or y > KNIGHT_STEP_SIZE:
      raise VectorAboveBoundsException(f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}")

    if y is None:
      raise NullYComponentException(f"{method} {NullYComponentException.DEFAULT_MESSAGE}")

    self._x = x
    self._y = y


  @property
  def x(self) -> int:
    return self._x


  @property
  def y(self) -> int:
    return self._y


  def __eq__(self, other):
    if other is self:
      return True
    if other is None:
      return False
    if not isinstance(other, Vector):
      return False

    return self._x == other.x and self._y == other.y


  def scalar_product(self, scalar: Scalar) -> 'Vector':
    return Vector(x=self._x * scalar.value, y=self._y * scalar.value)



  #
  # def add_to_coordinate(self, coord: Coord) -> Coord:
  #   validation_result = CoordinateSpecification.is_satisfied_by(coord)
  #   if not validation_result.is_success():
  #     raise validation_result.team_exception
  #
  #   c = validation_result.payload
  #
  #   row = c.row + self.y
  #   column = c.column + self.x
  #
  #   validation_result = CoordinateSpecification.is_satisfied_by(
  #     Coord(row=row, column=column)
  #   )
  #   if not validation_result.is_success():
  #     raise validation_result.team_exception
  #
  #   return validation_result.payload



  def __str__(self):
    return f"Vector(x={self._x}, y={self._y})"