# src/chess/rank/factory/exception.py

"""
Module: chess.rank.factory.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.rank import RankException
from chess.system import BuildFailedException

__all__ = [
    # ======================# RANK_BUILD_FAILED EXCEPTION #======================#
    "RankBuildFailedException",
]


# ======================# RANK_BUILD_FAILED EXCEPTION #======================#
class RankBuildFailedException(RankException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Rank build creates an exception. Failed check exceptions are encapsulated
        in an RankBuildFailedException which is sent to the caller in a BuildResult.
    2.  The RankBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   RankException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "RANK_BUILD_FAILED"
    DEFAULT_MESSAGE = "Rank build failed."