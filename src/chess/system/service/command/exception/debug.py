# src/chess/system/command/exception/debug.py

"""
Module: chess.system.command.exception.debug
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# COMMAND_DEBUG EXCEPTION #======================#
    "CommandDebugException",
]

from chess.system import CommandException, DebugException


# ======================# COMMAND_DEBUG EXCEPTION #======================#
class CommandDebugException(CommandException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes Command state that caused a failing result.

    # PARENT:
        *   DebugException
        *   CommandException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERR_CODE = "COMMAND_DEBUG_ERROR"
    MSG = "A Command experienced a state that raised a CommandDebugException."