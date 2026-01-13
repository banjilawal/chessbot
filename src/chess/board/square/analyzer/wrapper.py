# src/chess/board/square/analyzer/wrapper.py

"""
Module: chess.board.square.analyzer.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_SQUARE_RELATION_TEST_FAILURE EXCEPTION #======================#
    "BoardSquareRelationAnalysisFailedException",
]

from chess.system import RelationAnalysisFailedException


# ======================# BOARD_SQUARE_RELATION_TEST_FAILURE EXCEPTION #======================#
class BoardSquareRelationAnalysisFailedException(RelationAnalysisFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exception that kills the relation test process before the board-square relationship
        status has been evaluated.

    # PARENT:
        *   ExceptionWrapper

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_SQUARE_RELATION_TEST_FAILURE"
    DEFAULT_MESSAGE = "Board-Square relation analysis failed."