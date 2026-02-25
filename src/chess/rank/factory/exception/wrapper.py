# src/chess/rank/factory/exception/wrapper.py

"""
Module: chess.rank.factory.exception.wrapper
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.system import BuildException

__all__ = [
    # ======================# RANK_BUILD_FAILURE #======================#
    "RankBuildException",
]


# ======================# RANK_BUILD_FAILURE #======================#
class RankBuildException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in RankBuilder.build that, prevented BuildResult.success() from 
        being returned.

    # PARENT:
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "RANK_BUILD_FAILED"
    MSG = "Rank build failed."