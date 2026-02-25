# src/chess/square/service/menu/operation/exception/super.py

"""
Module: chess.square.service.menu.operation.exception.super
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
      *   ServiceOperationException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERROR_CODE = "SQUARE_BUILD_OPERATION_ERROR"
    DEFAULT_MESSAGE = "SquareBuildOperatio raised an exception."