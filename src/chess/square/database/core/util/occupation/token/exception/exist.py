# src/chess/square/database/core/util/occupation/token/exception/exist.py

"""
Module: chess.square.database.core.util.occupation.token.exception.exist
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""



__all__ = [
    # ======================# SQUARE_NOT_FOUND EXCEPTION #======================#
    "SquareNotFoundException",
]

from chess.square import SquareDebugException


# ======================# SQUARE_NOT_FOUND EXCEPTION #======================#
class SquareNotFoundException(SquareDebugException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failure UpdateResult was returned because a tkone wanted to occupy a square which does not exist in
    the SquareStack.

    # PARENT:
        *   SquareDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_NOT_FOUND_ERROR"
    DEFAULT_MESSAGE = "SquareVisit start failed: token wanted to visit square which does not exist."