# src/chess/agent/service/exception.py

"""
Module: chess.agent.service.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ServiceException

__all__ = [
    "AgentServiceException",
]

class AgentServiceException(ServiceException):
    ERROR_CODE = "AGENT_SERVICE_ERROR"
    DEFAULT_ERROR_CODE = "AgentService raised an exception."