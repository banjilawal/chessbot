# src/chess/agent/context/service/exception/missing/builder.py

"""
Module: chess.agent.context.service.exception.missing.builder
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import InvalidAgentContextServiceException

__all__ = [
    #======================# AGENT_CONTEXT SERVICE EXCEPTIONS #======================#
    "MissingAgentContextBuilderException",
]


#======================# AGENT_CONTEXT SERVICE EXCEPTIONS #======================#
class MissingAgentContextBuilderException(InvalidAgentContextServiceException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    Indicate an attempt was made to add a duplicate item o a collection that only allows uniques.

    # PARENT
        *   InvalidAgentContextServiceException

    # PROVIDES:
    MissingAgentContextBuilderException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "MISSING_AGENT_CONTEXT_BUILDER_ERROR"
    DEFAULT_MESSAGE = "AgentContextService does not have the required AgentContextBuilder."