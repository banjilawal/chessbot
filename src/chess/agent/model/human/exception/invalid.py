# src/chess/agent/model/human/exception/invalid.py

"""
Module: chess.agent.model.human.exception.invalid
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import HumanAgentException
from chess.system import ValidationException

__all__ = [
    # ======================# AGENT_CONTEXT VALIDATION SUPER CLASS #======================#
    "InvalidHumanAgentException",
]


# ======================# AGENT_CONTEXT VALIDATION SUPER CLASS #======================#
class InvalidHumanAgentException(HumanAgentException, ValidationException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised HumanAgent validation.
    2.  Wraps unhandled exceptions that hit the finally-block in HumanAgentValidator methods.

    # PARENT
        *   HumanAgentException
        *   ValidationException

    # PROVIDES:
    InvalidHumanAgentException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "HUMAN_AGENT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "HumanAgent validation failed."