# src/chess/board/occupant/analyzer/wrapper.py

"""
Module: chess.board.occupant.analyzer.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_TOKEN_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
    "BoardTokenAnalysisException",
]

from chess.system import AnalysisException


# ======================# BOARD_TOKEN_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
class BoardTokenAnalysisException(AnalysisException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exception that kills the relation test process before the board-occupant relationship
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
    ERROR_CODE = "BOARD_TOKEN_RELATION_ANALYSIS_FAILURE"
    DEFAULT_MESSAGE = "Board-Token relation analysis failed."