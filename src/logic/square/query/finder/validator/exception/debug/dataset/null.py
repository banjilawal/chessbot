# src/logic/square/validation/exception/debug/collider_candidates/model.py

"""
Module: logic.square.validation.exception.debug.collider_candidates.square
Author: Banji Lawal
Created: 2026-02-23
"""

from logic.square import SquareDebugException
from logic.system import SquareException

_all__ = [
    # ======================# NO_SQUARE_DATASOURCE_PROVIDED EXCEPTION #======================#
    "SquareDataSourceNullException",
]


# ======================# NO_SQUARE_DATASOURCE_PROVIDED EXCEPTION #======================#
class SquareDataSourceNullException(SquareDebugException, SquareException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  A failing SearchResult was returned because no collider_candidates was provided for the query.

    Super Class:
        *   SquareDebugException
        *   SquareException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_SQUARE_DATASOURCE_PROVIDED_EXCEPTION"
    MSG = "No square collider_candidates was provided. Received square instead."