# src/chess/agent/context/service/exception/base

"""
Module: chess.agent.context.service.exception.base
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
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # Parent
        *   ServiceException

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised when an AgentContextService's normal operations are halted
        by an error condition.
    2.  Raised when no specific exception exists for the error interrupting AgentContext processes from
        their normal flows.

    # PROVIDES:
    AgentContextException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "AgentContextService raised an exception."