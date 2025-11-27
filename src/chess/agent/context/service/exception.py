# src/chess/agent/context/service/exception.py

"""
Module: chess.agent.context.service.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ServiceException

__all__ = [
    # ======================# AGENT_CONTEXT SERVICE EXCEPTIONS #======================#
    "AgentContextServiceException",
]


# ======================# AGENT_CONTEXT SERVICE EXCEPTIONS #======================#
class AgentContextServiceException(ServiceException):
    ERROR_CODE = "AGENT_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "AgentContextService raised an exception."