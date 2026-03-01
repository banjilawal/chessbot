# src/logic/player/relation/wrapper.py

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
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exception that kills the relation test process before the agent-team relationship
        status has been evaluated.

    # PARENT:
        *   WorkerException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "AGENT_TEAM_RELATION_ANALYSIS_FAILURE"
    MSG = "AgentTeamRelationTest failed."
