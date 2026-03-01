# src/logic/player/model/machine/exception.py

"""
Module: logic.player.model.machine.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from logic.player import PlayerException

__all__ = [
    #======================# MACHINE_PLAYER EXCEPTION #======================#
    "MachinePlayerException",
]

#======================# MACHINE_PLAYER EXCEPTION #======================#
class MachinePlayerException(PlayerException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate an attribute, method, or operation organic to a MachinePlayer encountered a condition which
        caused a failure.
    2.  Wraps an exception that hits the try-finally block of an Player method.

    # PARENT:
        *   PlayerException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "MACHINE_PLAYER_EXCEPTION"
    MSG = "MachinePlayer raised an exception."
    