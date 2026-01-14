# src/chess/system/validate/exception.py

"""
Module: chess.system.validate.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import WrapperException

__all__ = [
    # ======================# RELATION_TEST_FAILED EXCEPTION #======================#
    "RelationAnalysisFailedException",
]


# ======================# RELATION_TEST_FAILED EXCEPTION #======================#
class RelationAnalysisFailedException(WrapperException):
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
    ERROR_CODE = "RELATION_TEST_FAILED_ERROR"
    DEFAULT_MESSAGE = "RelationTest failed."
