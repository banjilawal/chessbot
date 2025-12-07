# src/chess/agent/service/data/exception/invalid.py

"""
Module: chess.agent.service.data.exception.invalid
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationException
from chess.agent import AgentDataServiceException


__all__ = [
    # ======================# AGENT_DATA_SERVICE VALIDATION EXCEPTIONS #======================#
    "InvalidAgentDataServiceException",
]

# ======================# AGENT_DATA_SERVICE VALIDATION EXCEPTIONS #======================#
class InvalidAgentDataServiceException(AgentDataServiceException, ValidationException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during AgentDataService verification process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an AgentDataServiceValidator method.

    # PARENT
        *   AgentDataServiceException
        *   ValidationException

    # PROVIDES:
    InvalidAgentDataServiceException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_DATA_SERVICE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "AgentDataService validation failed."