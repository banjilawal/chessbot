# src/chess/board/token/analyzer/wrapper.py

"""
Module: chess.board.token.analyzer.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_TOKEN_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
    "BoardTokenAnalysisFailedException",
]

from chess.system import AnalysisFailedException


# ======================# BOARD_TOKEN_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
class BoardTokenAnalysisFailedException(AnalysisFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exception that kills the relation test process before the board-token relationship
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