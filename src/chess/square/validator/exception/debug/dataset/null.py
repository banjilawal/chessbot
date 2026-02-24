# src/chess/square/validator/exception/debug/dataset/null.py

"""
Module: chess.square.validator.exception.debug.dataset.null
Author: Banji Lawal
Created: 2026-02-23
"""

from chess.square import SquareDebugException
from chess.system import NullException

_all__ = [
    # ======================# NO_SQUARE_DATASOURCE_PROVIDED EXCEPTION #======================#
    "SquareDataSourceNullException",
]


# ======================# NO_SQUARE_DATASOURCE_PROVIDED EXCEPTION #======================#
class SquareDataSourceNullException(SquareDebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing SearchResult was returned because no dataset was provided for the query.

    # PARENT:
        *   SquareDebugException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_SQUARE_DATASOURCE_PROVIDED_ERROR"
    DEFAULT_MESSAGE = "No square dataset was provided. Received null instead."