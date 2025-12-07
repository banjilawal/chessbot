# src/chess/agent/context/service/exception/invalid.py

"""
Module: chess.agent.context.service.exception.invalid
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationException
from chess.agent import AgentContextServiceException


__all__ = [
    # ======================# AGENT_CONTEXT_SERVICE VALIDATION EXCEPTIONS #======================#
    "InvalidAgentContextServiceException",
]


# ======================# AGENT_CONTEXT_SERVICE VALIDATION EXCEPTIONS #======================#
class InvalidAgentContextServiceException(AgentContextServiceException, ValidationException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during AgentContextService verification process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an AgentContextServiceValidator method.
    
    # PARENT
        *   AgentContextServiceException
        *   ValidationException

    # PROVIDES:
    InvalidAgentContextServiceException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_CONTEXT_SERVICE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "AgentContextService validation failed."