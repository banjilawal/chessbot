# src/logic/player/relation/worker.py

"""
Module: logic.player.relation.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# PLAYER_TEAM_RELATION_ANALYSIS_FAILURE #======================#
    "PlayerTeamAnalysisException",
]

from logic.system import AnalysisException


# ======================# PLAYER_TEAM_RELATION_ANALYSIS_FAILURE #======================#
class PlayerTeamAnalysisException(AnalysisException):
    """
    Role:Exception Wrapper, Encapsulation, Error Chaining

    Responsibilities:
    1.  Wrap any exception that kills the relation test process before the agent-team relationship
        status has been evaluated.

    Super Class:
        *   WorkException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "AGENT_TEAM_RELATION_ANALYSIS_FAILURE"
    MSG = "AgentTeamRelationTest failed."
