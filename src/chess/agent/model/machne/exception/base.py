# src/chess/agent/model/machine/exception/exception.py

"""
Module: chess.agent.model.machine.exception.base
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
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate an attribute, method, or operation organic to a MachineAgent encountered a condition which
        caused a failure.
    2.  Wraps unhandled exceptions that hit the try-finally block of an Agent method.

    # PARENT
        *   AgentException

    # PROVIDES:
    MachineAgentException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "MACHINE_AGENT_ERROR"
    DEFAULT_MESSAGE = "MachineAgent raised an exception."
    