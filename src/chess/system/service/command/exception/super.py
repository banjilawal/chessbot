# src/chess/system/service/command/exception/super.py

"""
Module: chess.system.service.command.exception.super
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# COMMAND EXCEPTION #======================#
    "CommandException",
]

from chess.system import SuperClassException


# ======================# COMMAND EXCEPTION #======================#
class CommandException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of CommandDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERR_CODE = "COMMAND_ERROR"
    MSG = "Command raised an exception."