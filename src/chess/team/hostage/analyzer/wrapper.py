# src/chess/team/prisoner/wrapper.py

"""
Module: chess.team.prisoner.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# HOSTAGE_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
    "HostageAnalysisFailedException",
]

from chess.system import AnalysisFailedException


# ======================# HOSTAGE_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
class HostageAnalysisFailedException(AnalysisFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exception that kills the relation test process before the team-prisoner relationship
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
    ERROR_CODE = "HOSTAGE_RELATION_ANALYSIS_FAILURE"
    DEFAULT_MESSAGE = "TeamHostageRelationTest failed."