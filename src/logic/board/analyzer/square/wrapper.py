# src/logic/board/item/analyzer/wrapper.py

"""
Module: logic.board.item.analyzer.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_SQUARE_RELATION_ANALYSIS_FAILURE #======================#
    "BoardSquareAnalysisException",
]

from logic.system import AnalysisException


# ======================# BOARD_SQUARE_RELATION_ANALYSIS_FAILURE #======================#
class BoardSquareAnalysisException(AnalysisException):
    """
    Role:Exception Wrapper, Encapsulation, Error Chaining

    Responsibilities:
    1.  Wrap any exception that kills the relation test process before the board-item relationship
        status has been evaluated.

    Super Class:
        *   WrapperException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "BOARD_SQUARE_RELATION_ANALYSIS_FAILURE"
    MSG = "Board-Square relation analysis failed."