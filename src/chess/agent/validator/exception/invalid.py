# src/chess/agent/number_bounds_validator/exception/exception.py

"""
Module: chess.agent.number_bounds_validator.exception.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentException
from chess.system import ValidationFailedException

__all__ = [
    #======================# AGENT VALIDATION EXCEPTION #======================#
    "InvalidAgentException",
]


#======================# AGENT VALIDATION EXCEPTION #======================#
class InvalidAgentException(AgentException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised during an PlayerAgent verification process.
    2.  Catchall Exception for AgentValidator when a candidate fails a sanity check.
    3.  Wraps unhandled exception that hit the try-finally block of an AgentValidator method.

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

