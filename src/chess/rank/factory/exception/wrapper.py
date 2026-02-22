# src/chess/rank/factory/exception/wrapper.py

"""
Module: chess.rank.factory.exception.wrapper
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.rank import RankException
from chess.system import BuildException

__all__ = [
    # ======================# RANK_BUILD_FAILURE #======================#
    "RankBuildException",
]


# ======================# RANK_BUILD_FAILURE #======================#
class RankBuildException(RankException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Rank build creates an exception. Failed check exceptions are encapsulated
        in an RankBuildException which is sent to the caller in a BuildResult.
    2.  The RankBuildException provides a trace for debugging and application recovery.

    # PARENT:
        *   RankException
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "RANK_BUILD_FAILED"
    DEFAULT_MESSAGE = "Rank build failed."