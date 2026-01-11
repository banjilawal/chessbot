# src/chess/board/validator/exception/registration.py

"""
Module: chess.board.validator.exception.registration
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.board import BoardValidationFailedException
from chess.system import RegistrationException

__all__ = [
# ======================# BOARD_NOT_REGISTERED_WITH_ARENA EXCEPTION #======================#
    "BoardNotRegisteredWithArenaException",
]


#======================# BOARD_NOT_REGISTERED_WITH_ARENA EXCEPTION #======================#
class BoardNotRegisteredWithArenaException(BoardValidationFailedException, RegistrationException):
    """
    Catchall for when a Board does not have a relationship with another entity.
    """
    ERROR_CODE = "BOARD_REGISTRATION_ERROR"
    DEFAULT_MESSAGE = "Board is not registered with parent."
    ERROR_CODE = "BOARD_NOT_REGISTERED_WITH_ARENA_ERROR"
    DEFAULT_MESSAGE = "Board is not registered with Arena. There is no relationship between them."