# src/chess/agent/service/exception.py

"""
Module: chess.agent.service.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ServiceException

__all__ = [
    # ======================# AGENT_SERVICE EXCEPTIONS #======================#
    "AgentServiceException",
]


# ======================# AGENT_SERVICE EXCEPTIONS #======================#
class AgentServiceException(ServiceException):
    """
    # ROLE: Builder, Data Integrity Guarantor

    # RESPONSIBILITIES:
    Produce Agent instances whose integrity is always guaranteed. If any attributes do not pass
    their integrity checks, send an exception instead of an unsafe Agent.

    # PARENT
        *   Builder

    # PROVIDES:
    BuildResult[Agent] containing either:
        - On success: Agent in the payload.
        - On failure: Exception.

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_SERVICE_ERROR"
    DEFAULT_ERROR_CODE = "AgentService raised an exception."