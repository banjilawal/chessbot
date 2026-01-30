# src/chess/board/item/analyzer/wrapper.py

"""
Module: chess.board.item.analyzer.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_SQUARE_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
    "BoardSquareAnalysisFailedException",
]

from chess.system import AnalysisFailedException


# ======================# BOARD_SQUARE_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
class BoardSquareAnalysisFailedException(AnalysisFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exception that kills the relation test process before the board-item relationship
        status has been evaluated.

    # PARENT:
        *   WrapperException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_SQUARE_RELATION_ANALYSIS_FAILURE"
    DEFAULT_MESSAGE = "Board-Square relation analysis failed."