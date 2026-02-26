# src/chess/square/validator/exception/debug/dataset/square.py

"""
Module: chess.square.validator.exception.debug.dataset.square
Author: Banji Lawal
Created: 2026-02-23
"""

from chess.square import SquareDebugException
from chess.system import SquareException

_all__ = [
    # ======================# NO_SQUARE_DATASOURCE_PROVIDED EXCEPTION #======================#
    "SquareDataSourceSquareException",
]


# ======================# NO_SQUARE_DATASOURCE_PROVIDED EXCEPTION #======================#
class SquareDataSourceSquareException(SquareDebugException, SquareException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing SearchResult was returned because no dataset was provided for the query.

    # PARENT:
        *   SquareDebugException
        *   SquareException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_SQUARE_DATASOURCE_PROVIDED_ERROR"
    MSG = "No square dataset was provided. Received square instead."