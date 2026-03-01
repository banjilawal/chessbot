# src/logic/board/context/validator/exception/debug/excess.py

"""
Module: logic.board.context.validator.exception.debug.excess
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from logic.system import ContextFlagCountException
from logic.board import BoardContextException

__all__ = [
    # ========================= ARENA_BOARD_CONTEXT_FLAG EXCEPTION =========================#
    "ArenaBoardContextFlagsException"
]


# ========================= ARENA_BOARD_CONTEXT_FLAG EXCEPTION =========================#
class ArenaBoardContextFlagsException(BoardContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  more than one BoardContext flag was enabled. Only one Board attribute-value-tuple can be used in
        a search.

    # PARENT:
        *   ContextFlagCountException
        *   BoardContextValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ARENA_BOARD_CONTEXT_FLAG_EXCEPTION"
    MSG = (
        "Arena BoardContext flags were set. an Board search can only use one-and-only "
        "map flag at a time."
    )
