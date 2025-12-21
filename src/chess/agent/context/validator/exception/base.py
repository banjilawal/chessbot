# src/chess/agent/context/validator/exception/base.py

"""
Module: chess.agent.context.validator.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentContextException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# AGENT_CONTEXT VALIDATION EXCEPTION #======================#
    "InvalidAgentContextException",
]


# ======================# AGENT_CONTEXT VALIDATION EXCEPTION #======================#
class InvalidAgentContextException(AgentContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised AgentContext validation.
    2.  Wraps unhandled exception that hit the finally-block in AgentContextValidator methods.
    
    # PARENT:
        *   AgentContextException
        *   ValidationFailedException

    # PROVIDES:
   None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "AgentContext validation failed."
