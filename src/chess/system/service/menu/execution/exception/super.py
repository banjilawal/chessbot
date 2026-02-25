# src/chess/system/service/menu/operation/exception/super.py

"""
Module: chess.system.service.menu.operation.exception.super
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# SERVICE_OPERATION EXCEPTION #======================#
    "ServiceOperationException",
]

from chess.system import SuperClassException


# ======================# SERVICE_OPERATION EXCEPTION #======================#
class ServiceOperationException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of ServiceOperationDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERROR_CODE = "SERVICE_OPERATION_ERROR"
    DEFAULT_MESSAGE = "ServiceOperation raised an exception."