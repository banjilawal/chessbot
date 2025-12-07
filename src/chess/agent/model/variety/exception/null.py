# src/chess/agent/model/variety/exception/null.py

"""
Module: chess.agent.model.variety.exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.agent import InvalidAgentVarietyException

__all__ = [
    # ======================# AGENT_VARIETY NULL EXCEPTION #======================#
    "AgentVarietyNullException",
]

# ======================# NULL AGENT_VARIETY EXCEPTION  #======================#
class AgentVarietyNullException(InvalidAgentVarietyException, NullException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during Agentt build process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an AgentBuilder method.

    # PARENT
        *   AgentException
        *   BuildFailedException

    # PROVIDES:
    BuildResult[Agent] containing either:
            - On success: Agent in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
    None
    """
    """"""
    ERROR_CODE = "NULL_AGENT_VARIETY_ERROR"
    DEFAULT_MESSAGE = "AgentVariety cannot be null."


