# src/chess/square/database/core/util/stats/exception/catchall.py

"""
Module: chess.square.database.core.util.stats.exception.catchall
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

___all__ = [
    # ======================# SQUARE_STACK_ANALYZER EXCEPTION #======================#
    "SquareStackAnalyzerException",
]

from chess.system import ChessException

# ======================# SQUARE_STACK_ANALYZER EXCEPTION #======================#
class SquareStackAnalyzerException(ChessException):
    """
    # ROLE: Class/Module Identifier, Exception Chain Layer 3, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate a failure occurred in SquareStackAnalyzer.
    2.  The method where the error occurred is identified in the exception nested directly underneath.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_STACK_ANALYZER_ERROR"
    MSG = "SquareStackAnalyzer raised an exception."