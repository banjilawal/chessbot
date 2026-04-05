# src/logic/player/relation/validator.py

"""
Module: logic.player.relation.work
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# PLAYER_TEAM_RELATION_ANALYSIS_FAILURE #======================#
    "PlayerTeamAnalysisException",
]

from system import AnalysisException


# ======================# PLAYER_TEAM_RELATION_ANALYSIS_FAILURE #======================#
class PlayerTeamAnalysisException(AnalysisException):
    """
    Role:Exception Work, Encapsulation, Error Chaining

    Responsibilities:
    1.  Wrap any exception that kills the relation test exception before the agent-team relationship
        status has been evaluated.

    Super Class:
        *   WorkException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "AGENT_TEAM_RELATION_ANALYSIS_FAILURE"
    MSG = "AgentTeamRelationTest failed."
