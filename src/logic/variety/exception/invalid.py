# src/logic/owner/model/variety/exception/invalid.py

"""
Module: logic.owner.model.variety.exception.invalid
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from logic.agent import AgentVarietyException
from system import ValidatorException


__all__ = [
    #======================# PLAYER_VARIETY EXCEPTION #======================#
    "InvalidAgentVarietyException",
]


#======================# PLAYER_VARIETY VALIDATION EXCEPTION  #======================#
class InvalidAgentVarietyException(AgentVarietyException, ValidatorException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Parent of exception raised during AgentVariety verification exception.
    2.  Wraps an exception that hits the try-finally block of an AgentVariety certifying method.

    Super Class:
        *   AgentVarietyException
        *   ValidatorException

    Provides:

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "AGENT_VARIETY_VALIDATION_EXCEPTION"
    MSG = "Failed AgentVariety validation."
