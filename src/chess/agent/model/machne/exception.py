# src/chess/agent/model/exception.py

"""
Module: chess.agent.model.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentException

__all__ = [
    # ======================# MACHINE_AGENT EXCEPTION #======================#
    "MachineAgentException",
]


# ======================# MACHINE_AGENT EXCEPTION #======================#
class MachineAgentException(AgentException):
    ERROR_CODE = "MACHINE_AGENT_ERROR"
    DEFAULT_MESSAGE = "MachineAgent raised an exception."
    
