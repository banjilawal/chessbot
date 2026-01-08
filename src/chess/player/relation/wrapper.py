# src/chess/player/relation/wrapper.py

"""
Module: chess.player.relation.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# PLAYER_TEAM_RELATION_TEST_FAILURE EXCEPTION #======================#
    "AgentTeamRelationAnalysisFailedException",
]

from chess.system import RelationAnalysisFailedException


# ======================# PLAYER_TEAM_RELATION_TEST_FAILURE EXCEPTION #======================#
class AgentTeamRelationAnalysisFailedException(RelationAnalysisFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exception that kills the relation test process before the agent-team relationship
        status has been evaluated.

    # PARENT:
        *   ExceptionWrapper

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_TEAM_RELATION_TEST_FAILURE"
    DEFAULT_MESSAGE = "AgentTeamRelationTest failed."
