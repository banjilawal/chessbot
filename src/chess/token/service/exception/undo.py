# src/chess/token/service/exception/unopened.py

"""
Module: chess.token.service.exception.unopened
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.token import TokenException

__all__ = [
    # ======================# OVER_MOVE_UNDO_LIMIT EXCEPTION #======================#
    "OverMoveUndoLimitException",
]


# ======================# OVER_MOVE_UNDO_LIMIT EXCEPTION #======================#
class OverMoveUndoLimitException(TokenException, NullException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that a occupant.positions.undo_coord_push failed because no Coord had been added since the last undo.
        Allowing more than one undo means more than one turn can be undone.

    # PARENT:
        *   TeamDaaServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "OVER_MOVE_UNDO_LIMIT_ERROR"
    DEFAULT_MESSAGE = "Token.positions.undo_coord_push failed: Cannot undo two moves."
