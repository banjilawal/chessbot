# src/logic/owner/model/variety/exception/invalid.py

"""
Module: logic.owner.model.variety.exception.invalid
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from logic.agent import AgentVarietyException
from logic.system import ValidationException


__all__ = [
    #======================# PLAYER_VARIETY EXCEPTION #======================#
    "InvalidAgentVarietyException",
]


#======================# PLAYER_VARIETY VALIDATION EXCEPTION  #======================#
class InvalidAgentVarietyException(AgentVarietyException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Parent of exception raised during AgentVariety verification process.
    2.  Wraps an exception that hits the try-finally block of an AgentVariety certifying method.

    # PARENT:
        *   AgentVarietyException
        *   ValidationException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "AGENT_VARIETY_VALIDATION_EXCEPTION"
    MSG = "Failed AgentVariety validation."
