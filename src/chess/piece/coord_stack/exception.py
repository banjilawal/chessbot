from chess.exception import ChessException, ValidationException, NullException

__all__ = [
  'CoordStackException',
  'DoubleCoordPushException',
  'NullCoordStackException',
  'CoordStackValidationException'
]

"""
Super class for Piece exceptions
"""
class CoordStackException(ChessException):
  """
  Super class for exceptions raised by CoordStack objects
  """
  ERROR_CODE = "COORD_STACK_ERROR"
  DEFAULT_MESSAGE = "CoordStack raised an exception."


class DoubleCoordPushException(CoordStackException):
  """
  Raised when a Coord at the top of the stack is pushed again. This is additional sanity check.
  Piece should catch moving to the same Square before the stack is modified. important in OccupationEvent
  transactions
  """
  ERROR_CODE = "DOUBLE_COORD_PUSH_ERROR"
  DEFAULT_MESSAGE = "Cannot push the same Coord twice. The Coord is already at the top of the stack"


class NullCoordStackException(CoordStackException, NullException):
  """Raised a CoordStack is null. A null CoordStack indicates a corrupted Piece state"""
  ERROR_CODE = "NULL_COORD_STACK_ERROR"
  DEFAULT_MESSAGE = f"CoordStack is null. This should never happen because Piece must always have a CoordStack"


class CoordStackValidationException(CoordStackException, ValidationException):
  ERROR_CODE = "COORDINATE_STACK_VALIDATION_ERROR"
  DEFAULT_MESSAGE = f"CoordinateStack validation failed"