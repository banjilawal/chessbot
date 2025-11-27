# src/chess/agent/validator/exception/exception.py

"""
Module: chess.agent.validator.exception.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentException
from chess.system import ValidationException

__all__ = [
    # ======================# AGENT VALIDATION EXCEPTION SUPER CLASS #======================#
    "InvalidAgentException",
]

# ======================# AGENT VALIDATION EXCEPTION SUPER CLASS #======================#
class InvalidAgentException(AgentException, ValidationException):
    """
    Catchall Exception for AgentValidator when a validation candidate fails a sanity check. Super
    class of all Agent validation exceptions.
    """
    ERROR_CODE = "AGENT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Agent validation failed."

