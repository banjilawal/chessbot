# src/chess/board/validator/exception/registration/registration.py

"""
Module: chess.board.validator.exception.registration.registration
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.board import InvalidBoardException
from chess.system import RegistrationException

__all__ = [
    #======================# BOARD_REGISTRATION EXCEPTIONS #======================#
    "BoardRegistrationException",
    "BoardNotRegisteredWithGameException",
]


#======================# BOARD_REGISTRATION EXCEPTIONS #======================#
class BoardRegistrationException(InvalidBoardException, RegistrationException):
    """
    Catchall for when a Board does not have a relationship with another entity.
    """
    ERROR_CODE = "BOARD_REGISTRATION_ERROR"
    DEFAULT_MESSAGE = "Board is not registered with parent."


class BoardNotRegisteredWithGameException(BoardRegistrationException):
    ERROR_CODE = "BOARD_NOT_REGISTERED_WITH_GAME_ERROR"
    DEFAULT_MESSAGE = "Board is not registered with Game. There is no relationship between them."