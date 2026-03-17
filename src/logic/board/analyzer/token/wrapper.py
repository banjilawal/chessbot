# src/logic/board/occupant/analyzer/wrapper.py

"""
Module: logic.board.occupant.analyzer.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_TOKEN_RELATION_ANALYSIS_FAILURE #======================#
    "BoardTokenAnalysisException",
]

from logic.system import AnalysisException


# ======================# BOARD_TOKEN_RELATION_ANALYSIS_FAILURE #======================#
class BoardTokenAnalysisException(AnalysisException):
    """
    Role:Exception Wrapper, Encapsulation, Error Chaining

    Responsibilities:
    1.  Wrap any exception that kills the relation test process before the board-occupant relationship
        status has been evaluated.

    Super Class:
        *   WrapperException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "BOARD_TOKEN_RELATION_ANALYSIS_FAILURE"
    MSG = "Board-Token relation analysis failed."