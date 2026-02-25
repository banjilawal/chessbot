# src/chess/system/service/menu/route/exception/super.py

"""
Module: chess.system.service.menu.route.exception.super
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# SERVICE_ROUTE EXCEPTION #======================#
    "ServiceRouteException",
]

from chess.system import SuperClassException


# ======================# SERVICE_ROUTE EXCEPTION #======================#
class ServiceRouteException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of ServiceRouteDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERR_CODE = "SERVICE_ROUTE_ERROR"
    MSG = "CommandRouter raised an exception."