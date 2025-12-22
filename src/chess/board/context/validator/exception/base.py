# src/chess/board/map/validator/exception/exception.py

"""
Module: chess.board.map.validator.exception.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.board import BoardContextException

__all__ = [
    #======================# BOARD_CONTEXT VALIDATION EXCEPTION #======================#
    "InvalidBoardContextException",
]

#======================# BOARD_CONTEXT VALIDATION EXCEPTION #======================#
class InvalidBoardContextException(BoardContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised BoardContext validation.
    2.  Wrap an exception that hits the try-finally-block in BoardContextValidator methods.
    
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
