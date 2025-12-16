# src/chess/player_agent/model/machine/exception/build.py

"""
Module: chess.player_agent.model.machine.exception.build
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentBuildFailedException, MachineAgentException

__all__ = [
    #======================# MACHINE_AGENT EXCEPTION #======================#
    "MachineAgentBuildFailedException",
]

#======================# MACHINE_AGENT BUILD EXCEPTIONS #======================#
class MachineAgentBuildFailedException(MachineAgentException, AgentBuildFailedException):
    """
    # ROLE:

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during MachineAgent build process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an MachineAgentBuilder method.

    # PARENT:
        *   MachineAgentException
        *   AgentBuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "MACHINE_AGENT_BUILD_ERROR"
    DEFAULT_ERROR_CODE = "MachineAgent build failed."