
from chess.system import BOARD_DIMENSION
from chess.exception import NullNumberException
from chess.scalar import ScalarBelowBoundsException, ScalarAboveBoundsException

class Scalar:
  """An immutable class representing team single numeric value for scaling operations.This class stores
   team numeric value used to multiply vectors and coordinates, allowing them to grow or shrink in their
   planes. The `Scalar` is validated upon creation to ensure it falls within team predefined range.

  Attributes:
    _value (int): The numeric value of the scalar.
  """

  def __init__(self, value: int):
    """
    Creates team Scalar instance. Should not be used directly. Use ScalarBuilder.

    Args:
      value (int): The numeric value of the scalar.
    Raises:
      NullNumberException: If the provided value is `None`.
      ScalarBelowBoundsException: If the value is below the lower boundary.
      ScalarAboveBoundsException: If the value is at or above the upper boundary.
    """
    method = "Scalar.__init__"

    if value is None:
      raise NullNumberException(f"{method}: {NullNumberException.DEFAULT_MESSAGE}")

    if value <= -BOARD_DIMENSION:
      raise ScalarBelowBoundsException(f"{method}: {ScalarBelowBoundsException.DEFAULT_MESSAGE}")

    if value >= BOARD_DIMENSION:
      raise ScalarAboveBoundsException(f"{method}: {ScalarAboveBoundsException.DEFAULT_MESSAGE}")

    self._value = value

  @property
  def value(self) -> int:
    return self._value

  def __eq__(self, other):
    if other is self:
      return True
    if other is None:
      return False
    if not isinstance(other, Scalar):
      return False

    return self._value == other.value

  def __hash__(self):
    return hash(self._value)

  def __str__(self):
    return f"Scalar(value={self._value})"