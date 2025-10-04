# chess.arena.exception

"""
Module: `chess.arena.exception`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
Responsibilities: Holds exceptions organic to `Arena` objects

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
    ERROR_CODE = "ARENA_ERROR"
    DEFAULT_MESSAGE = "Arena raised an exception."


# === ARENA VALIDATION EXCEPTIONS ===
class NullArenaException(ArenaException, NullException):
    """Raised if an entity, method, or operation requires a arena but gets null instead."""
    ERROR_CODE = "NULL_ARENA_ERROR"
    DEFAULT_MESSAGE = "Arena cannot be null"


class InvalidArenaException(ArenaException, ValidationException):
    """
    Raised by ArenaValidator if arena fails sanity checks. Exists primarily to catch all exceptions raised
    validating an existing arena
    """
    ERROR_CODE = "ARENA_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Arena validation failed"


# === ARENA BUILD EXCEPTIONS ===
class ArenaBuildFailedException(ArenaException, BuildFailedException):
    """
    Raised when ArenaBuilder encounters an error while building a team. Exists primarily to catch all
    exceptions raised build a new arena
    """
    ERROR_CODE = "ARENA_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Arena build failed."