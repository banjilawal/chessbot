# src/chess/board/context/validator/exception/exception.py

"""
Module: chess.board.context.validator.exception.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.board import BoardContextException

__all__ = [
    #======================# BOARD_CONTEXT VALIDATION SUPER CLASS #======================#
    "InvalidBoardContextException",
]

#======================# BOARD_CONTEXT VALIDATION SUPER CLASS #======================#
class InvalidBoardContextException(BoardContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised BoardContext validation.
    2.  Wraps unhandled exceptions that hit the finally-block in BoardContextValidator methods.
    
    # PARENT:
        *   BoardContextException
        *   ValidationFailedException

    # PROVIDES:
   None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "BoardContext validation failed."
