# src/chess/agent/entity_service/exception/missing/builder.py

"""
Module: chess.agent.entity_service.exception.missing.builder
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import InvalidAgentServiceException

__all__ = [
    # ======================# AGENT_SERVICE EXCEPTIONS #======================#
    "MissingAgentBuilderException",
]


# ======================# AGENT_SERVICE EXCEPTIONS #======================#
class MissingAgentBuilderException(InvalidAgentServiceException):
    """
    # ROLE: Error Tracing, Debugging

    # PARENT
        *   InvalidAgentServiceException

    # RESPONSIBILITIES:
    1.  Indicate an AgentService was constructed with either no AgentBuilder or the wrong
        type of object.

    # PROVIDES:
    MissingAgentBuilderException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "MISSING_AGENT_BUILDER_ERROR"
    DEFAULT_MESSAGE = "AgentService does not have the required AgentBuilder."