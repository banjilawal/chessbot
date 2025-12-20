# src/chess/game/context/service/exception/operation.py

"""
Module: chess.game.context.service.exception.operation
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import OperationFailedException
from chess.game import GameContextServiceException

__all__ = [
    #======================# OPERATION GAME_CONTEXT_SERVICE EXCEPTION #======================#
    "GameContextServiceOperationFailedException",
]


#======================# GAME_CONTEXT_SERVICE OPERATION EXCEPTION #======================#
class GameContextServiceOperationFailedException(GameContextServiceException, OperationFailedException):
    """
    # ROLE: Error Tracing, Debugging, Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicates a ameContextService method that returns a Result object caught an unhandled exception
        in its try-catch-finally block.

    # PARENT:
        *   GameContextServiceException
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_CONTEXT_SERVICE_OPERATION_ERROR"
    DEFAULT_MESSAGE = "GameContextService operation failed."