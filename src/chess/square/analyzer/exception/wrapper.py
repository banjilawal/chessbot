# src/chess/square/analyzer/exception/wrapper.py

"""
Module: chess.square.analyzer.exception.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_TOKEN_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
    "SquareTokenAnalysisException",
]

from chess.system import AnalysisException


# ======================# SQUARE_TOKEN_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
class SquareTokenAnalysisException(AnalysisException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exception that kills the relation test process before the item-occupant relationship
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