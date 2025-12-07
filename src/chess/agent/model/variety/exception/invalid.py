# src/chess/agent/model/variety/exception/invalid.py

"""
Module: chess.agent.model.variety.exception.invalid
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationException
from chess.agent import AgentVarietyException

__all__ = [
    # ======================# AGENT_VARIETY EXCEPTION #======================#
    "InvalidAgentVarietyException",
]

# ======================# AGENT_VARIETY VALIDATION EXCEPTION  #======================#
class InvalidAgentVarietyException(AgentVarietyException, ValidationException):
    """"""
    ERROR_CODE = "AGENT_VARIETY_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Failed AgentVariety validation."


