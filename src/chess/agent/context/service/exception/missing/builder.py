# src/chess/agent/context/service/exception/missing/builder.py

"""
Module: chess.agent.context.entity_service.exception.missing.builder
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import InvalidAgentContextServiceException

__all__ = [
    # ======================# AGENT_CONTEXT SERVICE EXCEPTIONS #======================#
    "MissingAgentContextBuilderException",
]


# ======================# AGENT_CONTEXT SERVICE EXCEPTIONS #======================#
class MissingAgentContextBuilderException(InvalidAgentContextServiceException):
    """
    # ROLE: Error Tracing, Debugging

    # PARENT
        *   InvalidAgentContextServiceException

    # RESPONSIBILITIES:
    1.  Indicate an AgentContextService was constructed with either no AgentContextBuilder or the wrong
        type of object.

    # PROVIDES:
    MissingAgentContextBuilderException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "MISSING_AGENT_CONTEXT_BUILDER_ERROR"
    DEFAULT_MESSAGE = "AgentContextService does not have the required AgentContextBuilder."