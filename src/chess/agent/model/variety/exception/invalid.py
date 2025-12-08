# src/chess/agent/model/variety/exception/invalid.py

"""
Module: chess.agent.model.variety.exception.invalid
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentVarietyException
from chess.system import ValidationFailedException


__all__ = [
    # ======================# AGENT_VARIETY EXCEPTION #======================#
    "InvalidAgentVarietyException",
]


# ======================# AGENT_VARIETY VALIDATION EXCEPTION  #======================#
class InvalidAgentVarietyException(AgentVarietyException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during AgentVariety verification process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an AgentVariety certifying method.

    # PARENT
        *   AgentVarietyException
        *   ValidationFailedException

    # PROVIDES:
    InvalidAgentVarietyException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_VARIETY_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Failed AgentVariety validation."
