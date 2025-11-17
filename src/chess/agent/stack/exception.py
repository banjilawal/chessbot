# src/chess/agent/stack/exception.py

"""
Module: chess.agent.stack.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.exception import ChessException, ValidationException, NullException

__all__ = [
  'CoordStackException',

  'NullCoordStackException',
  'CoordStackValidationException'
]

from chess.system import InconsistentCollectionException

"""
Super class for Piece exceptions
"""
class CoordStackException(InconsistentCollectionException):
  """
  Super class for exceptions raised by CoordStack objects
  """
  ERROR_CODE = "COORD_STACK_ERROR"
  DEFAULT_MESSAGE = "CoordStack raised an rollback_exception."
  
  
class CoordStakOperationException(CoordStackException):
  pass
  
class CoordStackConsistencyException(CoordStackException, InconsistentCollectionException):
  pass


class PopEmptyStackException(CoordStackException):
  """Raised when trying to pop from empty stack."""
  ERROR_CODE = "POP_EMPTY_STACK_ERROR"
  DEFAULT_MESSAGE = "Cannot pop from empty stack"

class DuplicatePushException(CoordStackException):
  """Raised when trying to push duplicate to stack that doesn'candidate allow duplicates."""
  ERROR_CODE = "DUPLICATE_PUSH_ERROR"
  DEFAULT_MESSAGE = "Cannot push duplicate item to stack"


class NullCoordStackException(CoordStackException, NullException):
  """Raised team_name CoordStack is null. A null CoordStack indicates team_name corrupted Piece state"""
  ERROR_CODE = "NULL_COORD_STACK_ERROR"
  DEFAULT_MESSAGE = f"CoordStack is null. This should never happen because Piece must always have team_name CoordStack"


class CoordStackValidationException(CoordStackException):
  ERROR_CODE = "COORDINATE_STACK_VALIDATION_ERROR"
  DEFAULT_MESSAGE = f"CoordinateStack validation failed."








class PushNullException(CoordStackException):
  """Raised when trying to push null item to stack."""
  ERROR_CODE = "PUSH_NULL_ERROR"
  DEFAULT_MESSAGE = "Cannot push null item to stack"


class InconsistentCurrentCoordException(CoordStackException):
  ERROR_CODE = "INCONSISTENT_CURRENT_COORD_ERROR"
  DEFAULT_MESSAGE = "Current coordinate state is inconsistent"