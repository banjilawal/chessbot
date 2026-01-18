# src/chess/system/validate/exception.py

"""
Module: chess.system.validate.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import WrapperException

__all__ = [
    # ======================# RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
    "AnalysisFailedException",
]


# ======================# RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
class AnalysisFailedException(WrapperException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exception that kills the relation test process before the status has been evaluated.

    # PARENT:
        *   WrapperException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "RELATION_ANALYSIS_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Relation analysis failed."
