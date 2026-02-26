# src/chess/square/service/command/exception/super.py

"""
Module: chess.square.service.command.exception.super
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# SQUARE_BUILD_COMMAND EXCEPTION #======================#
    "SquareBuildCommand",
]

from chess.system.service.command.exception.super import ServiceCommandException


# ======================# SQUARE_BUILD_COMMAND EXCEPTION #======================#
class SquareBuildCommand(ServiceCommandException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of ServiceCommandDebugException

  # PARENT:
      *   CommandException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERR_CODE = "SQUARE_BUILD_COMMAND_ERROR"
    MSG = "SquareBuildOperatio raised an exception."