# src/chess/agent/context/base.py

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
    
    # PARENT
        *   AgentException
        *   ContextException

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised when an AgentContext's organic fields or methods run into a condition that
        leads to an operation failing.
    2.  Parent of exceptions raised by AgentContext Builders and Validators or any other classes that highly
        cohere with AgentContext objects.
    3.  Catchall for AgentContext failure states that are not covered by a lower level AgentContext exception.

    # PROVIDES:
    AgentContextException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_CONTEXT_ERROR"
    DEFAULT_ERROR_CODE = "AgentContext raised an exception."