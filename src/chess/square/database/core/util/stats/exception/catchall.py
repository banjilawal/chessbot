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
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by SquareStackAnalyzer methods that return Result objects.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_STACK_ANALYZER_ERROR"
    DEFAULT_MESSAGE = "SquareStackAnalyzer raised an exception."