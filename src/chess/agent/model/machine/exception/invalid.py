# src/chess/agent/model/machine/exception/invalid.py

"""
Module: chess.agent.model.machine.exception.invalid
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import MachineAgentException
from chess.system import ValidationFailedException

__all__ = [
    #======================# AGENT_CONTEXT VALIDATION SUPER CLASS #======================#
    "InvalidMachineAgentException",
]


#======================# AGENT_CONTEXT VALIDATION SUPER CLASS #======================#
class InvalidMachineAgentException(MachineAgentException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised MachineAgent validation.
    2.  Wraps unhandled exceptions that hit the finally-block in MachineAgentValidator methods.

    # PARENT
        *   MachineAgentException
        *   ValidationFailedException

    # PROVIDES:
    InvalidMachineAgentException

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "MACHINE_AGENT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "MachineAgent validation failed."