# src/chess/owner/relation/wrapper.py

"""
Module: chess.owner.relation.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# PLAYER_TEAM_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
    "PlayerTeamAnalysisFailedException",
]

from chess.system import AnalysisFailedException


# ======================# PLAYER_TEAM_RELATION_ANALYSIS_FAILURE EXCEPTION #======================#
class PlayerTeamAnalysisFailedException(AnalysisFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exception that kills the relation test process before the agent-team relationship
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
    ERROR_CODE = "AGENT_TEAM_RELATION_ANALYSIS_FAILURE"
    DEFAULT_MESSAGE = "AgentTeamRelationTest failed."
