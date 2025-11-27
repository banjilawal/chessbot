# src/chess/agent/model/human/exception.py

"""
Module: chess.agent.model.human.exception
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
    ERROR_CODE = "HUMAN_AGENT_ERROR"
    DEFAULT_MESSAGE = "HumanAgent raised an exception."