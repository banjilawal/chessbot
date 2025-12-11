# src/chess/agent/context/service/exception/missing/validator.py

"""
Module: chess.agent.context.service.exception.missing.validator
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import InvalidAgentContextServiceException

__all__ = [
    #======================# AGENT_CONTEXT SERVICE EXCEPTIONS #======================#
    "MissingAgentContextValidatorException",
]


class MissingAgentContextValidatorException(InvalidAgentContextServiceException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    Indicate an AgentContextService was constructed with either no AgentContextBuilder or the wrong
    type of object.

    # PARENT:
        *   InvalidAgentContextServiceException

    # PROVIDES:
    MissingAgentContextBuilderException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "MISSING_AGENT_CONTEXT_VALIDATOR_ERROR"
    DEFAULT_MESSAGE = "AgentContextService does not have the required AgentContextValidator."