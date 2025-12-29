# src/chess/agent/relation/wrapper.py

"""
Module: chess.agent.relation.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# AGENT_TEAM_RELATION_TEST_FAILURE EXCEPTION #======================#
    "AgentTeamRelationTestFailedException",
]

from chess.system import RelationTestFailedException


# ======================# AGENT_TEAM_RELATION_TEST_FAILURE EXCEPTION #======================#
class AgentTeamRelationTestFailedException(RelationTestFailedException):
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
