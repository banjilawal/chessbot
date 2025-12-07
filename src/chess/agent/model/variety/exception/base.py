# src/chess/agent/model/variety/exception/base.py

"""
Module: chess.agent.model.variety.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# AGENT_VARIETY EXCEPTION #======================#
    "AgentVarietyException",
]


# ======================# AGENT_VARIETY EXCEPTION  #======================#
class AgentVarietyException(ChessException):
    """
    Super class for exceptions raised by AgentVariety objects. DO NOT USE DIRECTLY. Subclasses
    give more useful debugging messages.
    """
    ERROR_CODE = "AGENT_VARIETY_ERROR"
    DEFAULT_MESSAGE = "AgentVariety raised an exception."