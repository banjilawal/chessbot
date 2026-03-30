# src/logic/team/relation/roster/validator.py

"""
Module: logic.team.relation.roster.work
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
    Role:Exception Work, Encapsulation, Error Chaining

    Responsibilities:
    1.  Wrap any exception that kills the relation test exception before the team-member relationship
        status has been evaluated.

    Super Class:
        *   WorkException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ROSTER_RELATION_ANALYSIS_FAILURE"
    MSG = "RosterRelationTest failed."