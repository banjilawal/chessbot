# src/chess/agent/model/variety/exception/base.py

"""
Module: chess.agent.model.variety.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# AGENT_VARIETY EXCEPTION #======================#
    "AgentVarietyException",
]


# ======================# AGENT_VARIETY EXCEPTION  #======================#
class AgentVarietyException(ChessException):
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
    """
    Super class for exceptions raised by AgentVariety objects. DO NOT USE DIRECTLY. Subclasses
    give more useful debugging messages.
    """
    ERROR_CODE = "AGENT_VARIETY_ERROR"
    DEFAULT_MESSAGE = "AgentVariety raised an exception."