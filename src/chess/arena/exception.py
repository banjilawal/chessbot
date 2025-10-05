# chess.arena.exception

"""
Module: `chess.arena.exception`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
 Provides: Holds exceptions organic to `Arena` objects

Contains: See the list of exception in the __alL__ list following
"""

from chess.system import ChessException, NullException, BuildFailedException, ValidationException

__all__ = [
  'ArenaException',

  # === ARENA VALIDATION EXCEPTIONS ===
  'NullArenaException',
  'InvalidArenaException',

  # === ARENA BUILD EXCEPTIONS ===
  'ArenaBuildFailedException',

  # === COLLECTION_ARENA EXCEPTONS ===
]

class ArenaException(ChessException):
  """
  Super class exceptions Class object raises organically. Do not use directly. Subclasses give
  details useful for debugging. ClassException exists primarily to allow catching all class
  exceptions.
  """
  ERROR_CODE = "ARENA_ERROR"
  DEFAULT_MESSAGE = "Arena raised an exception."


# === ARENA VALIDATION EXCEPTIONS ===
class NullArenaException(ArenaException, NullException):
  """Raised if an entity, method, or operation requires an arena but gets null instead."""
  ERROR_CODE = "NULL_ARENA_ERROR"
  DEFAULT_MESSAGE = "Arena cannot be null"


class InvalidArenaException(ArenaException, ValidationException):
  """
  Raised by ArenaValidator if arena fails sanity checks. Exists primarily to
  catch all exceptions raised validating an existing arena
  """
  ERROR_CODE = "ARENA_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Arena validation failed"


# === ARENA BUILD EXCEPTIONS ===
class ArenaBuildFailedException(ArenaException, BuildFailedException):
  """
  Raised when ArenaBuilder crashed while building a new arena. Exists
  primarily to catch all exceptions raised creating arenas.
  """
  ERROR_CODE = "ARENA_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Arena build failed."