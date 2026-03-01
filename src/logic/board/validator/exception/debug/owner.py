# src/logic/owner/service/exception/different.py

"""
Module: logic.owner.service.exception.different
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

___all__ = [
    # ======================# BOARD_OWNED_BY_DIFFERENT_ARENA EXCEPTION #======================#
    "BoardBelongsToDifferentOwnerException",
]

from logic.board import BoardException
from logic.arena import ArenaException


# ======================# BOARD_OWNED_BY_DIFFERENT_ARENA EXCEPTION #======================#
class BoardOwnedByDifferentArenaException(BoardException, ArenaException):
    """
    # ROLE: Error Tracing, Debugging
    
    # RESPONSIBILITIES:
    1.  Indicate that a board was not validated because its owner because its arena relationship was mismatched."

    # PARENT:
        *   ArenaException
        *   BoardException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "BOARD_OWNED_BY_DIFFERENT_ARENA"
    MSG = "Board validation failed: The board belongs to a different arena."