# src/chess/agent/context/exception.py

"""
Module: chess.agent.context.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextException


__all__ = [
    # ======================# AGENT_CONTEXT EXCEPTION SUPER CLASS #======================#
    "AgentContextException",
]


# ======================# AGENT_CONTEXT EXCEPTION SUPER CLASS #======================#
class AgentContextException(ContextException):
    ERROR_CODE = "AGENT_CONTEXT_ERROR"
    DEFAULT_ERROR_CODE = "AgentContext raised an exception."