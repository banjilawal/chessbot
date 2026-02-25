# src/chess/system/service/menu/execution/exception/super.py

"""
Module: chess.system.service.menu.execution.exception.super
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# SERVICE_EXECUTION EXCEPTION #======================#
    "ServiceExecutionException",
]

from chess.system import SuperClassException


# ======================# SERVICE_EXECUTION EXCEPTION #======================#
class ServiceExecutionException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of ServiceExecutionDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERR_CODE = "SERVICE_EXECUTION_ERROR"
    MSG = "ServiceExecution raised an exception."