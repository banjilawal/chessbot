# src/chess/agent/model/human/exception/base.py

"""
Module: chess.agent.model.human.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentException

__all__ = [
    # ======================# HUMAN_AGENT EXCEPTION #======================#
    "HumanAgentException",
]

# ======================# HUMAN_AGENT EXCEPTION #======================#
class HumanAgentException(AgentException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate an attribute, method, or operation organic to a HumanAgent encountered a condition which
        caused a failure.
    2.  Wraps unhandled exceptions that hit the try-finally block of an Agent method.

    # Parent
        *   AgentException

    # PROVIDES:
    HumanAgentException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "HUMAN_AGENT_ERROR"
    DEFAULT_MESSAGE = "HumanAgent raised an exception."
    