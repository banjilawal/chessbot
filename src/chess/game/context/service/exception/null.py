# src/chess/game/context/service/exception/null.py

"""
Module: chess.game.context.service.exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.game import InvalidGameContextServiceException

__all__ = [
    #======================# NULL GAME_CONTEXT_SERVICE EXCEPTIONS #======================#
    "NullGameContextServiceException",
]


#======================# NULL GAME_CONTEXT_SERVICE EXCEPTION #======================#
class NullGameContextServiceException(InvalidGameContextServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate if an entity, method or operation required an GameContextService but got null instead.
    
    # PARENT:
        *   InvalidGameContextServiceException
        *   NullException

    # PROVIDES:
    NullGameContextServiceException

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_GAME_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "GameContextService cannot be null."