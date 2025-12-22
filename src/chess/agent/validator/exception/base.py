# src/chess/agent/validator/exception/_base.py

"""
Module: chess.agent.validator.exception._base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# INVALID_AGENT EXCEPTION #======================#
    "InvalidAgentException",
]


#======================# INVALID_AGENT EXCEPTION #======================#
class InvalidAgentException(AgentException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised during an PlayerAgent verification process.
    2.  Catchall Exception for AgentValidator when a candidate fails a sanity check.
    3.  Wraps an exception that hits the try-finally block of an AgentValidator method.

    # PARENT:
        *   AgentException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "PlayerAgent validation failed."

