# src/chess/agent/model/exception.py

"""
Module: chess.agent.model.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# AGENT EXCEPTION SUPER CLASS #======================#
    "AgentException",
]

# ======================# AGENT EXCEPTION SUPER CLASS #======================#
class AgentException(ChessException):
    """
    Super class for exceptions raised by Agent objects. DO NOT USE DIRECTLY. Subclasses
    give more useful debugging messages.
    """
    ERROR_CODE = "AGENT_ERROR"
    DEFAULT_MESSAGE = "Agent raised an exception."