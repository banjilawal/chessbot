# src/chess/system/validate/exception.py

"""
Module: chess.system.validate.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import OperationFailedException

__all__ = [
    # ======================# RELATION_ANALYSIS_FAILURE #======================#
    "AnalysisException",
]


# ======================# RELATION_ANALYSIS_FAILURE #======================#
class AnalysisException(OperationFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why an analysis operation failed. The exception chain
        traces the ultimate source of failure.

    # PARENT:
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "RELATION_ANALYSIS_FAILURE"
    DEFAULT_MESSAGE = "Relation analysis failed."
