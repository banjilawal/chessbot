# src/chess/board/validator/exception/registration/arena.py

"""
Module: chess.board.validator.exception.registration.arena
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.board import BoardException
from chess.system import NotRegisteredException

__all__ = [
    # ======================# BOARD_NOT_REGISTERED_WITH_ARENA EXCEPTION #======================#
    "BoardNotSubmittedArenaRegistrationException",
]


# ======================# _NOT_REGISTERED_WITH_ARENA EXCEPTION #======================#
class BoardNotSubmittedArenaRegistrationException(BoardException, NotRegisteredException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate was not granted Board certification because its arena had a null board.

    # PARENT:
        *   BoardException
        *   NotRegisteredException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_NOT_REGISTERED_WITH_ARENA_ERROR"
    DEFAULT_MESSAGE = "Board validation failed: Its arena.board is null."