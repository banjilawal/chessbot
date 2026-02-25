# src/chess/square/service/menu/route/exception/super.py

"""
Module: chess.square.service.menu.route.exception.super
Author: Banji Lawal
Created: 2026-02-24
"""

__all__ = [
    # ======================# SERVICE_ROUTE EXCEPTION #======================#
    "ServiceRouteException",
]

from chess.square import SuperClassException


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
    ERROR_CODE = "SERVICE_ROUTE_ERROR"
    DEFAULT_MESSAGE = "ServiceRoute raised an exception."