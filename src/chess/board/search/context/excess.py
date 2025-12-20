# src/chess/board/context/number_bounds_validator/exception/flag/excess.py

"""
Module: chess.board.context.number_bounds_validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""


from chess.system import BoundsException
from chess.board import InvalidBoardContextException


__all__ = [
    # ========================= EXCESSIVE_BOARD_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessiveBoardContextFlagsSetException"
]

# ========================= EXCESSIVE_BOARD_CONTEXT_FLAG EXCEPTION =========================#
class ExcessiveBoardContextFlagsSetException(InvalidBoardContextException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates more than one BoardContext flag was enabled. Only one Board attribute-value tuple can be used in
        a search.

    # PARENT:
        *   BoundsException
        *   InvalidBoardContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESSIVE_BOARD_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "Excessive BoardContext flags were set. Only one BoardContext flag is allowed."
