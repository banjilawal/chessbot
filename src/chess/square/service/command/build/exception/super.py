# src/chess/square/service/operation/exception/super.py

"""
Module: chess.square.service.operation.exception.super
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# SQUARE_BUILD_OPERATION EXCEPTION #======================#
    "SquareBuildOperation",
]

from chess.system.service.operation.exception.super import ServiceOperationException


# ======================# SQUARE_BUILD_OPERATION EXCEPTION #======================#
class SquareBuildOperation(ServiceOperationException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of ServiceOperationDebugException

  # PARENT:
      *   CommandException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERR_CODE = "SQUARE_BUILD_OPERATION_ERROR"
    MSG = "SquareBuildOperatio raised an exception."