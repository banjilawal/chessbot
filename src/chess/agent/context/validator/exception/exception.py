# src/chess/player_agent/context/validator/exception/exception.py

"""
Module: chess.player_agent.context.validator.exception.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.agent import AgentContextException

__all__ = [
    #======================# AGENT_CONTEXT VALIDATION SUPER CLASS #======================#
    "InvalidAgentContextException",
]

#======================# AGENT_CONTEXT VALIDATION SUPER CLASS #======================#
class InvalidAgentContextException(AgentContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised AgentContext validation.
    2.  Wraps unhandled exceptions that hit the finally-block in AgentContextValidator methods.
    
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
