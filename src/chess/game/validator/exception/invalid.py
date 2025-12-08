# src/chess/agent/validator/exception/exception.py

"""
Module: chess.agent.validator.exception.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# AGENT VALIDATION EXCEPTION SUPER CLASS #======================#
    "InvalidAgentException",
]


# ======================# AGENT VALIDATION EXCEPTION SUPER CLASS #======================#
class InvalidAgentException(AgentException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during an Agent verification process.
    2.  Catchall Exception for AgentValidator when a candidate fails a sanity check.
    3.  Wraps unhandled exceptions that hit the try-finally block of an AgentValidator method.

    # PARENT
        *   AgentException
        *   ValidationFailedException

    # PROVIDES:
    InvalidAgentException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Agent validation failed."

