# src/chess/agent/model/machine/exception.py

"""
Module: chess.agent.model.machine.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentException

__all__ = [
    #======================# MACHINE_AGENT EXCEPTION #======================#
    "MachineAgentException",
]

#======================# MACHINE_AGENT EXCEPTION #======================#
class MachineAgentException(AgentException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate an attribute, method, or operation organic to a MachineAgent encountered a condition which
        caused a failure.
    2.  Wraps an exception that hits the try-finally block of an PlayerAgent method.

    # PARENT:
        *   AgentException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "MACHINE_AGENT_ERROR"
    DEFAULT_MESSAGE = "MachineAgent raised an exception."
    