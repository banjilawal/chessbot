# src/chess/system/err/number/exception/base.py

"""
Module: chess.system.err.number.exception.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# NUMBER EXCEPTION #======================#
    "FailsafeBranchExitPointException",
]


# ======================# NUMBER EXCEPTION #======================#
class FailsafeBranchExitPointException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate That  one or more terminating execution routes was not handled in branching conditions.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FAIL_SAFE_BRANCH_EXIT_POINT_ERROR"
    DEFAULT_MESSAGE = (
        "One or more result generating routes was not handled with an if-block. Check the possible outcomes "
        "and see if there is a missing execution flow."
    )