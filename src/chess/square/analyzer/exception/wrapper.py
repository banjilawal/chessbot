# src/chess/square/analyzer/exception/wrapper.py

"""
Module: chess.square.analyzer.exception.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_TOKEN_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
    "SquareTokenAnalysisFailedException",
]

from chess.system import AnalysisFailedException


# ======================# SQUARE_TOKEN_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
class SquareTokenAnalysisFailedException(AnalysisFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exception that kills the relation test process before the square-occupant relationship
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
    ERROR_CODE = "SQUARE_TOKEN_RELATION_ANALYSIS_FAILURE"
    DEFAULT_MESSAGE = "Square-Token relation analysis failed."