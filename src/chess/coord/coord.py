from typing import cast


from chess.vector import Vector, VectorValidator
from chess.scalar import Scalar, ScalarValidator

class Coord:
  _row: int
  _column: int

  def __init__(self, row: int, column: int):
    method = "Coord.__init__"

    # if row is None:
    #   raise NullRowException(f"{method} {NullRowException.DEFAULT_MESSAGE}")
    # if row < 0 or row >= ROW_SIZE:
    #   raise RowBelowBoundsException(
    #     f"{method} Row value {row} is out of bounds. "
    #     f"Must be between 0 and {ROW_SIZE - 1} inclusive."
    #   )
    # if column is None:
    #   raise NullColumnException(f"{method} {NullColumnException.DEFAULT_MESSAGE}")
    # if column < 0 or column >= COLUMN_SIZE:
    #   raise ColumnBelowBoundsException(
    #     f"{method} Column value {column} is out of bounds. "
    #     f"Must be between 0 and {COLUMN_SIZE - 1} inclusive."
    #   )
    self._row = row
    self._column = column


  @property
  def row(self) -> int:
    return self._row

  @property
  def column(self) -> int:
    return self._column


  def __eq__(self, other):
    if other is self:
      return True
    if other is None:
      return False
    if not isinstance(other, Coord):
      return False
    return self._row == other.row and self._column == other.column


  def __hash__(self):
    return hash((self._row, self._column))


  def __str__(self):
    return f"Coord(row:{self._row} column:{self._column})"


  def scalar_product(self, scalar: Scalar):
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
    method = "scalar_product"

    validation = ScalarValidator.validate(scalar)
    if not validation.is_success():
      raise validation.exception

    c = cast(validation.payload, Scalar)
    return Coord(row=self._row * c.ransom, column =self._column * c.ransom)


  def add_vector(self, vector: Vector) -> 'Coord':
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
    method = "add_vector"


    validation = VectorValidator.validate(vector)
    if not validation.is_success():
      raise validation.exception

    v = cast(validation.payload, Vector)
    return Coord(row =self._row + v.y, column =self._column + v.x)

