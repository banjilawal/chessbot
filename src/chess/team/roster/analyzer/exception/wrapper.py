# src/chess/team/relation/roster/wrapper.py

"""
Module: chess.team.relation.roster.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# ROSTER_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
    "RosterRelationAnalysisFailedException",
]

from chess.team import RosterServiceException


# ======================# ROSTER_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
class RosterRelationAnalysisFailedException(RosterServiceException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exception that kills the relation test process before the team-member relationship
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
    ERROR_CODE = "ROSTER_RELATION_ANALYSIS_FAILURE"
    DEFAULT_MESSAGE = "RosterRelationTest failed."