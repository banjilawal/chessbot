# src/chess/hostage/exception.py

"""
Module: chess.hostage.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# HOSTAGE EXCEPTION #======================#
    "HostageException",
]

from chess.system import SuperClassException


# ======================# HOSTAGE EXCEPTION #======================#
class HostageException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of HostageDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERR_CODE = "HOSTAGE_ERROR"
    MSG = "Hostage raised an exception."