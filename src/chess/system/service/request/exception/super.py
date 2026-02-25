# src/chess/system/service/request/exception/super.py

"""
Module: chess.system.service.request.exception.super
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# SERVICE_REQUEST EXCEPTION #======================#
    "ServiceRequestException",
]

from chess.system import SuperClassException


# ======================# SERVICE_REQUEST EXCEPTION #======================#
class ServiceRequestException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of ServiceRequestDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERR_CODE = "SERVICE_REQUEST_ERROR"
    MSG = "ServiceRequest raised an exception."