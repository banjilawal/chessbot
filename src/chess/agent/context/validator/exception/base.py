# src/chess/agent/validator/exception/base.py

"""
Module: chess.agent.validator.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentContextException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# AGENT_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidAgentContextException",
]


# ======================# AGENT_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidAgentContextException(AgentContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a AgentContext candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidAgentContextException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The InvalidAgentContextException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   AgentContextException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "AgentContext validation failed."