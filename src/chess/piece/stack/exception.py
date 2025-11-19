# src/chess/piece/stack/exception.py

"""
Module: chess.piece.stack.exception
Author: Banji Lawal
Created: 2025-09-30
version: 1.0.0
"""


from chess.system import ChessException, ValidationException, NullException


__all__ = [
  "CoordStackException",
  
  # ======================# NULL COORD_STACK EXCEPTIONS #======================#
  "NullCoordStackException",
  
  # ======================# COORD_STACK VALIDATION EXCEPTIONS #======================#
  "InvalidCoordStackException",
  "CoordStackSizeConflictException",
  "InconsistentCurrentCoordException",
  "CorruptedCoordStackException",
  
  # ======================# COORD_STACK OPERATION EXCEPTIONS #======================#
  "PoppingEmptyCoordStackException",
  "PushingDuplicateCoordException",
  "PushingNullException",
  
  # ======================# COORD_STACK_SERVICE EXCEPTIONS #======================#
  "CoordStackServiceException",
  
  # ======================# NULL COORD_STACK_SERVICE EXCEPTIONS #======================#
  "NullCoordStackServiceException",
  
  # ======================# COORD_STACK VALIDATION EXCEPTIONS #======================#
  "InvalidCoordStackServiceException",
]


class CoordStackException(ChessException):
  """
  Super class for exceptions raised by CoordStack objects. DO NOT USE DIRECTLY. Subclasses
  give more useful debugging messages.
  """
  ERROR_CODE = "COORD_STACK_ERROR"
  DEFAULT_MESSAGE = "CoordStack raised an exception."


# ======================# NULL COORD_STACK EXCEPTIONS #======================#
class NullCoordStackException(CoordStackException, NullException):
  """Raised if an entity, method, or operation requires CoordStack but gets null instead."""
  ERROR_CODE = "NULL_COORD_STACK_ERROR"
  DEFAULT_MESSAGE = "CoordStack cannot be null."


# ======================# COORD_STACK VALIDATION EXCEPTIONS #======================#
class InvalidCoordStackException(CoordStackException, ValidationException):
  """Catchall Exception for CoordStackValidator when a validation candidate fails a sanity check."""
  ERROR_CODE = "COORD_STACK_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "CoordStack validation failed."


class CoordStackSizeConflictException(CoordStackException, ValidationException):
  """Raised if coord_stack.size and coord_stack.is_empty() contradict each other."""
  ERROR_CODE = "COORD_STACK_SIZE_CONFLICT_ERROR"
  DEFAULT_MESSAGE = "CoordStack.size and CoordStack.is_empty() give contradictory results."


class InconsistentCurrentCoordException(CoordStackException, ValidationException):
  """Raised if coord_stack.current_coord is not null but the stack is empty or vice versa."""
  ERROR_CODE = "INCONSISTENT_CURRENT_COORD_ERROR"
  DEFAULT_MESSAGE = "The CoordStack.current_coord CoordStack.is_empty() contradict each other."


class CorruptedCoordStackException(CoordStackException, ValidationException):
  """Raised if the list is null. That is CoordStack.items is null"""
  ERROR_CODE = "CORRUPTED_COORD_STACK_ERROR"
  DEFAULT_MESSAGE = "CoordStack.items is null. There is inconsistent data in the system."


# ======================# COORD_STACK OPERATION EXCEPTIONS #======================#
class PoppingEmptyCoordStackException(CoordStackException):
  """Raised when trying to pop from an empty CoordStack."""
  ERROR_CODE = "POPPING_EMPTY_STACK_ERROR"
  DEFAULT_MESSAGE = "Cannot pop from an empty CoordStack."


class PushingDuplicateCoordException(CoordStackException):
  """Raised when trying to push the same coord onto the stack."""
  ERROR_CODE = "PUSHING_DUPLICATE_COORD_ERROR"
  DEFAULT_MESSAGE = "Cannot push duplicate coord onto the stack. All Coords must be unique."


class PushingNullException(CoordStackException):
  """Raised when trying to push null item to stack."""
  ERROR_CODE = "PUSHING_NULL_ERROR"
  DEFAULT_MESSAGE = "Cannot push null item onto a CoordStack."


# ======================# COORD_STACK_SERVICE EXCEPTIONS #======================#
class CoordStackServiceException(ChessException):
  """
  Super class for exceptions raised by CoordStackService objects. DO NOT USE DIRECTLY. Subclasses
  give more useful debugging messages.
  """
  ERROR_CODE = "COORD_STACK_SERVICE_ERROR"
  DEFAULT_MESSAGE = "CoordStackService raised an exception."


# ======================# NULL COORD_STACK_SERVICE EXCEPTIONS #======================#
class NullCoordStackServiceException(CoordStackServiceException, NullException):
  """Raised if an entity, method, or operation requires CoordStackService but gets null instead."""
  ERROR_CODE = "NULL_COORD_STACK_SERVICE_ERROR"
  DEFAULT_MESSAGE = "CoordStackService cannot be null."


# ======================# COORD_STACK VALIDATION EXCEPTIONS #======================#
class InvalidCoordStackServiceException(CoordStackServiceException, ValidationException):
  """Catchall Exception for CoordStackServiceValidator when a validation candidate fails a sanity check."""
  ERROR_CODE = "COORD_STACK_SERVICE_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "CoordStackService validation failed."