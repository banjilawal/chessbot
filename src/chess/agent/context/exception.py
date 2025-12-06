# src/chess/agent/context/exception.py

"""
Module: chess.agent.context.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentException
from chess.system import ContextException


__all__ = [
    # ======================# AGENT_CONTEXT EXCEPTION SUPER CLASS #======================#
    "AgentContextException",
]


# ======================# AGENT_CONTEXT EXCEPTION SUPER CLASS #======================#
class AgentContextException(AgentException, ContextException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
    
    # Parent
        *   AgentException
        *   ContextException

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised when an AgentContext's fields, methods, Builders and Validators.
        encounter an error condition.
    2.  Raised when no specific exception exists for the error interrupting AgentContext processes from
        their normal flows.

    # PROVIDES:
    AgentContextException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_CONTEXT_ERROR"
    DEFAULT_ERROR_CODE = "AgentContext raised an exception."