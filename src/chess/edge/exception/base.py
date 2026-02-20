# src/chess/edge/exception/base.py

"""
Module: chess.edge.exception.base
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

__all__ = [
    # ======================# EDGE EXCEPTION #======================#
    "EdgeException",
]

from chess.system import ChessException


# ======================# EDGE EXCEPTION #======================#
class EdgeException(ChessException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for Edge errors not covered by EdgeException subclasses.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "EDGE_ERROR"
    DEFAULT_MESSAGE = "Edge raised an exception."