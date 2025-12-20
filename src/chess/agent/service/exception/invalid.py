# src/chess/agent/service/exception/invalid.py

"""
Module: chess.agent.service.exception.invalid
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.agent import AgentServiceException


__all__ = [
    #======================# AGENT_SERVICE VALIDATION EXCEPTION #======================#
    "InvalidAgentServiceException",
]

#======================# AGENT_SERVICE VALIDATION EXCEPTION #======================#
class InvalidAgentServiceException(AgentServiceException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised during PlayerAgentService verification process.
    2.  Wraps unhandled exception that hit the try-finally block of an AgentServiceValidator method.

    # PARENT:
        *   AgentServiceException
        *   ValidationFailedException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_SERVICE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "PlayerAgentService validation failed."