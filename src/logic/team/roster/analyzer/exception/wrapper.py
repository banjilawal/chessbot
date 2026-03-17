# src/logic/team/relation/roster/wrapper.py

"""
Module: logic.team.relation.roster.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# ROSTER_RELATION_ANALYSIS_FAILURE #======================#
    "TeamRosterRelationAnalysisException",
]

from logic.team import TeamRosterException


# ======================# ROSTER_RELATION_ANALYSIS_FAILURE #======================#
class TeamRosterRelationAnalysisException(TeamRosterException):
    """
    Role:Exception Wrapper, Encapsulation, Error Chaining

    Responsibilities:
    1.  Wrap any exception that kills the relation test process before the team-member relationship
        status has been evaluated.

    Super Class:
        *   WrapperException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ROSTER_RELATION_ANALYSIS_FAILURE"
    MSG = "RosterRelationTest failed."